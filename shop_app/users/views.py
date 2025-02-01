from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('product_list')  # Przekierowanie jeśli użytkownik już jest zalogowany

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'product_list')  # Sprawdzenie czy jest przekierowanie
                return redirect(next_url)
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("home")  
