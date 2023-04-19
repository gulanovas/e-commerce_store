from . import views
from django.urls import path 

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remover_cart/<int:product_id>/', views.remover_cart, name='remover_cart'),
    path('remover_cart_item/<int:product_id>/', views.remover_cart_item, name='remover_cart_item'),
]
