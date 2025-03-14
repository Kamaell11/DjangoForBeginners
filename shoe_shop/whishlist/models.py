from django.db import models
from users.models import CustomUser
from shop.models import Shoe

class Wishlist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="wishlist")
    shoes = models.ManyToManyField(Shoe, related_name="wishlisted_by")

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
