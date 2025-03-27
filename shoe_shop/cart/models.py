from django.db import models
from decimal import Decimal
from django.conf import settings
from shop.models import Shoe

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        total = Decimal('0.00')
        for item in self.items.all():
            total += Decimal(str(item.shoe.price)) * Decimal(str(item.quantity))
        return total
    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.shoe.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.shoe.name} in {self.cart}"