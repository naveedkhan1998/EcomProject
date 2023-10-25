from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .models import Order, Product, OrderItem
import json


def loginPage(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    if request.method == "POST":
        username = request.POST.get("singin-email-temp")
        password = request.POST.get("singin-password-temp")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("Category")
        else:
            messages.info(request, "Username or password is incorrect")

    products = Product.objects.all()
    context = {"products": products, "order": order, "items": items}
    return render(request, "login.html", context)


def register(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.customer.name = form.cleaned_data.get("username")
            user.customer.email = form.cleaned_data.get("email")
            user.save()
            messages.success(request, "Account was Created")
            return redirect("Category")

    products = Product.objects.all()
    context = {"products": products, "order": order, "items": items, "form": form}
    return render(request, "login.html", context)


def logOut(request):
    logout(request)
    return redirect("login")


def category_boxed(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        customer = {}

    products = Product.objects.all()
    context = {
        "products": products,
        "order": order,
        "items": items,
        "customer": customer,
    }
    return render(request, "category-boxed.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        customer = {}

    context = {"items": items, "order": order, "customer": customer}
    return render(request, "cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        customer = {}

    context = {"items": items, "order": order, "customer": customer}
    return render(request, "checkout.html", context)


def updateitem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1

    if orderItem.quantity <= 0 or action == "delete":
        orderItem.delete()
    else:
        orderItem.save()

    return JsonResponse("Item was added", safe=False)
