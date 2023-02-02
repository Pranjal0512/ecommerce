from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cart', HomeView.as_view(), name='cart'),
    path('checkout', HomeView.as_view(), name='checkout'),
    path('contact', HomeView.as_view(), name='contact'),
    path('login', HomeView.as_view(), name='login'),
    path('my-account', HomeView.as_view(), name='my-account'),
    path('product-detail', HomeView.as_view(), name='product-detail'),
    path('product-list', HomeView.as_view(), name='product-list'),
    path('wishlist', HomeView.as_view(), name='wishlist'),
]
