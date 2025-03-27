from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm
from shop.models import Category, Shoe
from django.contrib.auth.decorators import login_required
from .forms import SimplePasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from cart.models import Cart, CartItem
from wishlist.models import Wishlist


def register_view(request):
    categories = Category.objects.all()
    cart_item_count = 0 

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')  
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.') 
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {
        'form': form,
        'categories': categories,
        'footer': True,
        'title': 'Registration',
        'cart_item_count': cart_item_count
    })

def login_view(request):
    categories = Category.objects.all()
    cart_item_count = 0

    if request.user.is_authenticated:
        return redirect('shop')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in successfully.')  
                next_url = request.GET.get('next', 'shop')
                return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')  
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {
        'form': form,
        'categories': categories,
        'footer': True,
        'title': 'Login',
        'cart_item_count': cart_item_count
    })

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')  
    return redirect("home")

def simple_password_reset_view(request):
    categories = Category.objects.all()
    cart_item_count = 0

    if request.method == "POST":
        form = SimplePasswordResetForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            new_password = form.cleaned_data["new_password"]
            user.set_password(new_password)
            user.save()

            update_session_auth_hash(request, user)
            
            messages.success(request, "Your password has been reset successfully.")  
            return redirect("login")
        else:
            messages.error(request, "Password reset failed. Please correct the errors.")  
    else:
        form = SimplePasswordResetForm()

    return render(request, "users/simple_password_reset.html", {
        "form": form,
        "categories": categories,
        "footer": True,
        "title": "Reset Password",
        "cart_item_count": cart_item_count
    })


@login_required
def account_view(request):
    cart_item_count = 0

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item_count = CartItem.objects.filter(cart=cart).count()

    # Pobierz wishlistę i produkty
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist_items = wishlist.shoes.all()

    orders = request.user.orders.all()  
    active_orders_count = orders.exclude(status="completed").count() if orders.exists() else 0  

    data = {
        'title': 'Account',
        'orders': orders,
        'active_orders_count': active_orders_count,
        'wishlist_items': wishlist_items, 
        'active_wishlist_count': wishlist_items.count(),
        'cart_item_count': cart_item_count,
    }
    return render(request, "users/account.html", data)


@login_required
def edit_address(request):
    if request.method == "POST":
        billing_address = request.POST.get("billing_address", "").strip()
        shipping_address = request.POST.get("shipping_address", "").strip()

        if billing_address and shipping_address:
            request.session["billing_address"] = billing_address
            request.session["shipping_address"] = shipping_address
            messages.success(request, "Address updated successfully!")
            return redirect("account")
        else:
            messages.error(request, "Both fields are required.")

    return render(request, "users/edit_address.html")