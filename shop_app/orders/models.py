from django.db import models
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Oczekujące'),
        ('shipped', 'Wysłane'),
        ('delivered', 'Dostarczone'),
        ('cancelled', 'Anulowane'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)
    shipped_date = models.DateTimeField(blank=True, null=True)
    delivered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Zamówienie {self.id} - {self.product.name} ({self.quantity})"
