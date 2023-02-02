from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cart', BaseView.as_view(), name='cart'),
    path('checkout', BaseView.as_view(), name='checkout'),
    path('contact', BaseView.as_view(), name='contact'),
    path('login', BaseView.as_view(), name='login'),
    path('my-account', BaseView.as_view(), name='my-account'),
    path('product-detail', BaseView.as_view(), name='product-detail'),
    path('product-list', BaseView.as_view(), name='product-list'),
    path('wishlist', BaseView.as_view(), name='wishlist'),
]
