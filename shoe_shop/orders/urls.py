from django.urls import path
from .views import order_list, thank_you, order_detail

urlpatterns = [
    path('', order_list, name='orders'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('thank-you/<int:order_id>/', thank_you, name='thank_you'),
]
