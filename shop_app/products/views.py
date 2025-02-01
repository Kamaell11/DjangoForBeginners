from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from orders.models import Order 


def is_customer_or_admin(user):
    return user.is_authenticated and user.role in ["customer", "admin"]

@login_required
def product_list(request):
    products = Product.objects.all()
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Order.objects.filter(user=request.user, status='pending').count()
    return render(request, 'products/product_list.html', {'products': products, 'cart_count': cart_count})

@login_required
def product_detail(request, pk):
    """Szczegóły produktu"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
@user_passes_test(is_customer_or_admin)
def product_add(request):
    """Dodawanie nowego produktu"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produkt został dodany!")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_add.html', {'form': form})

@login_required
@user_passes_test(is_customer_or_admin)
def product_edit(request, pk):
    """Edycja produktu"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produkt został zaktualizowany!")
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_edit.html', {'form': form, 'product': product})

@login_required
@user_passes_test(is_customer_or_admin)
def product_delete(request, pk):
    """Usuwanie produktu"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Produkt został usunięty!")
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})
