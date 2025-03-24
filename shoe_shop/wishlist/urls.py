from django.urls import path
from .views import wishlist_view, add_to_wishlist, remove_from_wishlist

urlpatterns = [
    path('', wishlist_view, name='wishlist'),
    path('remove/', remove_from_wishlist, name='remove_from_wishlist'),
    path('add/', add_to_wishlist, name='add_to_wishlist'),
]
