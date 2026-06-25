# shop/admin.py
from django.contrib import admin
from .models import Product, Cart, OrderItem,Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'created_at')
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'ordered_at')

admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)