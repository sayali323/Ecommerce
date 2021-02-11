from django.contrib import admin
from django.urls import path
from .views.home import Index , store , aboutUs
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart, checkout
from .views.contact import contact
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store/', store , name='store'),
    path('aboutUs/', aboutUs , name='aboutUs'),
    path('contact/', contact , name='contact'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('checkout', checkout , name='checkout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
