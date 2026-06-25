# shop/serializers.py
from rest_framework import serializers
from .models import Product, Cart, OrderItem
from .models import Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True) # Mengambil daftar item di dalam keranjang
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user_username', 'ordered', 'created_at', 'items']


class OrderSerializer(serializers.ModelSerializer):
    cart_details = CartSerializer(source='cart', read_only=True) 

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'ordered_at', 'cart_details']