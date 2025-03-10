from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Shoe
from .models import Cart, CartItem

@login_required
def add_to_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, shoe=shoe)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
        'title': 'Cart detail',
        'footer': True, 
        
        
        })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart:cart_detail')


@login_required
@require_POST
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = request.POST.get('quantity')
    if quantity and quantity.isdigit():
        cart_item.quantity = int(quantity)
        cart_item.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)