from django.db import models
from users.models import CustomUser
from shop.models import Shoe

class Review(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.shoe.name} ({self.rating}/5)"
