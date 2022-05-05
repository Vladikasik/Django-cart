from re import A
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('cart/', views.cart),
    path('add_product/<int:id>/', views.add_product)
]