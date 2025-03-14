from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Wishlist

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})
