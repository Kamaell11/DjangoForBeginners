from django.urls import path
from .views import order_list, order_detail, order_add, order_edit, order_delete

urlpatterns = [
    path('', order_list, name='order_list'),
    path('<int:pk>/', order_detail, name='order_detail'),
    path('add/', order_add, name='order_add'),
    path('<int:pk>/edit/', order_edit, name='order_edit'),
    path('<int:pk>/delete/', order_delete, name='order_delete'),
]
