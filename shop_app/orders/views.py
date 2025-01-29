from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    """Lista zamówień"""
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, pk):
    """Szczegóły zamówienia"""
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

def order_add(request):
    """Dodawanie nowego zamówienia"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_add.html', {'form': form})

def order_edit(request, pk):
    """Edycja zamówienia"""
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_edit.html', {'form': form, 'order': order})

def order_delete(request, pk):
    """Usuwanie zamówienia"""
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})
