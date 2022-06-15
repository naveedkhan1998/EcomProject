from django.urls import URLPattern, path
from . import views

urlpatterns = [ 
    path('',views.category_boxed,name="Category"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateitem,name="update_item"),
    path('register/',views.register,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logOut,name="logout"),
]