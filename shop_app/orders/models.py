from django.conf import settings
from products.models import Product
from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Oczekujące'),
        ('shipped', 'Wysłane'),
        ('delivered', 'Dostarczone'),
        ('cancelled', 'Anulowane'),
    ]
    phone_number = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    ordered_at = models.DateTimeField(auto_now_add=True)
    shipped_date = models.DateTimeField(blank=True, null=True)
    delivered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Zamówienie {self.id} - {self.product.name} ({self.quantity})by {self.user.username}"


