from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

class Cart(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=
                                  False) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Keranjang {self.user.username} - {'Selesai' if self.ordered else 'Aktif'}"

class OrderItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE) # 1 Nota berhubungan dengan 1 Keranjang yang sudah selesai
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota #{self.id} - {self.user.username} - Total: {self.total_price}"