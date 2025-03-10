from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:shoe_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]