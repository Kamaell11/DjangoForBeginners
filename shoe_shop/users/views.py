from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm
from shop.models import Category, Shoe
from django.contrib.auth.decorators import login_required
from .forms import SimplePasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
def register_view(request):
    categories = Category.objects.all()
    cart_item_count = 0  # Możesz dodać logikę liczenia elementów w koszyku

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')  # Dodaj komunikat
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')  # Dodaj komunikat o błędach
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
                messages.success(request, 'You have been logged in successfully.')  # Dodaj komunikat
                next_url = request.GET.get('next', 'shop')
                return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')  # Dodaj komunikat o błędzie
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
    messages.success(request, 'You have been logged out successfully.')  # Dodaj komunikat
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

            # Aktualizacja sesji, żeby użytkownik nie został wylogowany
            update_session_auth_hash(request, user)
            
            messages.success(request, "Your password has been reset successfully.")  # Dodaj komunikat
            return redirect("login")
        else:
            messages.error(request, "Password reset failed. Please correct the errors.")  # Dodaj komunikat o błędach
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
      data = {
       'title':'Account',
       'subTitle':'Shop',
       'subTitle2':'Account',
       'css':'<link rel="stylesheet" type="text/css" href="/static/css/variables/variable6.css"/>',
       'footer':'true',
       'script':'<script src="/static/js/vendors/zoom.js"></script>',
      }
      return render(request, "users/account.html", data)