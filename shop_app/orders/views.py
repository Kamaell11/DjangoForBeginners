from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Order
from .forms import OrderForm, CheckoutForm
def order_list(request):
    # Pobierz zamówienia z bazy danych
    orders = Order.objects.filter(user=request.user)
    
    # Liczba produktów w koszyku
    cart_count = orders.count()

    return render(request, 'orders/order_list.html', {
        'orders': orders,
        'cart_count': cart_count,
    })

def order_checkout(request):
    # Pobierz zamówienia użytkownika
    orders = Order.objects.filter(user=request.user)
    
    # Jeśli koszyk jest pusty, przekieruj na stronę główną lub koszyka
    if not orders.exists():
        return redirect('order_list')  # Możesz zmienić na stronę, na którą chcesz przekierować

    # Jeśli formularz jest przesyłany, zapisujemy dane
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Przetwórz dane formularza, np. zapisanie adresu dostawy i finalizacja zamówienia
            # Tu dodaj logikę zapisania zamówienia i/lub płatności
            form.save()  # Na przykład zapisanie danych do modelu Order, UserDetails itp.
            return redirect('order_success')  # Przekierowanie po udanym zamówieniu
    else:
        form = CheckoutForm()

    return render(request, 'orders/checkout.html', {
        'orders': orders,
        'form': form,
    })


def order_detail(request, pk):
    """Szczegóły zamówienia"""
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

def order_add(request, product_id):
    """Dodawanie produktu do koszyka"""
    product = get_object_or_404(Product, id=product_id)
    # Sprawdzamy, czy użytkownik ma już aktywne zamówienie
    order = Order.objects.filter(user=request.user, status='pending').first()
    
    if not order:
        # Jeśli brak aktywnego zamówienia, tworzymy nowe
        order = Order.objects.create(user=request.user, product=product, quantity=1, status='pending')
    else:
        # Jeśli zamówienie już istnieje, zwiększamy ilość produktu
        existing_order = Order.objects.filter(user=request.user, product=product, status='pending').first()
        if existing_order:
            existing_order.quantity += 1
            existing_order.save()
        else:
            Order.objects.create(user=request.user, product=product, quantity=1, status='pending')
    
    return redirect('order_list')

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
