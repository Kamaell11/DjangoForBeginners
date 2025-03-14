from django.shortcuts import render
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def order_list(request):
    orders = request.user.orders.all()
    return render(request, 'orders/order_list.html', {'orders': orders})