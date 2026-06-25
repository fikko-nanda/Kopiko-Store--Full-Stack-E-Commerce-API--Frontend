    # shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('products/', views.product_list, name='product-list'),
    path('cart/', views.view_cart, name='view-cart'),
    path('cart/add/', views.add_to_cart, name='add-to-cart'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order-history'),
]