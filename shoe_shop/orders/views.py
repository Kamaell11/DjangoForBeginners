from django.shortcuts import render, get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def order_list(request):
    orders = request.user.orders.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def thank_you(request, order_id):
    order = request.user.orders.get(id=order_id)
    return render(request, 'home/thankYou.html', {'order': order})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    cart_item_count = 0
    return render(request, 'orders/order_detail.html', {
        'order': order,
        'title': f'Order #{order.id}',
        'footer': True,
        'cart_item_count': cart_item_count
    })