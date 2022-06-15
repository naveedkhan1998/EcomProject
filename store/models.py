from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image
from django.dispatch import receiver

#The Customer Model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)
        instance.customer.save()

    def __str__(self):
        return self.name

#Product Model
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    #Returns set image if the product doesn't come with an Image
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/rainbow-love-heart-background-red-wood-60045149.jpg'
        return url

#Order/Cart Model
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200, null =True)

    def __str__(self):
        return str(self.id)

    #get the total price of items in the cart.
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        #get_total OrderItem property
        total = sum([item.get_total for item in orderitems])
        return total
    
    #get the total number of items in cart.
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        #quantity variable in OrderItem keeping track of each items quantity.
        total = sum([item.quantity for item in orderitems])
        return total


#Model for each item in Cart
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    #get total price of a given number of an orderitem
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address