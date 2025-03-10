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
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, shoe=shoe)
        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        cart_item_count = CartItem.objects.filter(cart=cart).count()
        request.session['cart_item_count'] = cart_item_count
    else:
      
        cart_item_count = request.session.get('cart_item_count', 0)
        request.session['cart_item_count'] = cart_item_count + 1

    return redirect('cart:cart')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    
   
    cart_item_count = cart_items.count()

    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
        'cart_items': cart_items,
        'cart_item_count': cart_item_count,  
        'title': 'Cart detail',
        'footer': True, 
    })
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()

    cart = Cart.objects.filter(user=request.user).first()
    cart_item_count = CartItem.objects.filter(cart=cart).count() if cart else 0
    request.session['cart_item_count'] = cart_item_count

    return redirect('cart:cart')

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