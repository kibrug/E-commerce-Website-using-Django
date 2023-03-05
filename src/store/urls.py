from django.contrib import admin
from django.urls import path
from .views.home import Index , store,home_View,search_View,search_View_Send

from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware

app_name="store"
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('home',home_View , name='home'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('search',search_View,name='search'),
    path('searchgets',search_View_Send,name='searchgets'),

]