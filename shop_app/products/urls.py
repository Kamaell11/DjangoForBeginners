from django.urls import path
from .views import product_list, product_detail, product_add, product_edit, product_delete

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/add/', product_add, name='product_add'),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
]
