from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from shop.models import Shoe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@login_required
def wishlist_view(request):

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = wishlist.shoes.all()  

    return render(request, 'wishlist/wishlist.html', {
        'wishlist_items': wishlist_items,
        })


@login_required
def account_view(request):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist_items = wishlist.shoes.all()
   
    return render(request, 'users/account.html', {
        'wishlist_items': wishlist_items,
      
    })

@login_required
def remove_from_wishlist(request):
    if request.method == "POST":
        shoe_id = request.POST.get("shoe_id")
        shoe = get_object_or_404(Shoe, id=shoe_id)
     
        wishlist = Wishlist.objects.get(user=request.user)
        
        wishlist.shoes.remove(shoe)
        
        return JsonResponse({"message": "Removed from wishlist", "removed": True})
    
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def add_to_wishlist(request):
    if request.method == "POST":
        shoe_id = request.POST.get("shoe_id")
        shoe = get_object_or_404(Shoe, id=shoe_id)
        
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        if shoe in wishlist.shoes.all():
            wishlist.shoes.remove(shoe)
            return JsonResponse({"message": "Removed from wishlist", "added": False})
        else:
            wishlist.shoes.add(shoe)
            return JsonResponse({"message": "Added to wishlist", "added": True})

    return JsonResponse({"error": "Invalid request"}, status=400)