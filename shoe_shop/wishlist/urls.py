from django.urls import path
from .views import wishlist_view

urlpatterns = [
    path('', wishlist_view, name='wishlist'),
]
