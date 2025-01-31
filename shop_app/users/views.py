from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from .forms import LoginForm
from .forms import RegisterForm



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Rejestracja zakończona sukcesem!")
            return redirect('home')  
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Użyj `request` jako pierwszego argumentu
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Zalogowano pomyślnie!')
                return redirect('product_list')  # Przekieruj do strony po zalogowaniu
            else:
                messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.')
        else:
            messages.error(request, 'Nieprawidłowe dane formularza.')
    else:
        form = LoginForm(request)  # Użyj `request` jako pierwszego argumentu
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Wylogowano pomyślnie!')
    return redirect("home")

def logout_view(request):
    logout(request)
    return redirect("home")