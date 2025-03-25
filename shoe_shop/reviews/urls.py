from django.urls import path
from .views import product_reviews

urlpatterns = [
    path("product/<int:shoe_id>/reviews/", product_reviews, name="product_reviews"),
]
