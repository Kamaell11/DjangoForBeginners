from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()  # Pobieramy wszystkie produkty
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Pobieramy produkt na podstawie jego ID
    return render(request, 'products/product_detail.html', {'product': product})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Przekierowanie na stronę listy produktów
    else:
        form = ProductForm()
    return render(request, 'products/product_add.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_edit.html', {'form': form, 'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')  # Przekierowanie na stronę listy produktów