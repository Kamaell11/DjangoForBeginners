from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), 
        label="Hasło"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), 
        label="Potwierdź hasło"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if not password1 or not password2:
            raise ValidationError("Hasło i potwierdzenie hasła są wymagane.")

        if password1 != password2:
            raise ValidationError("Hasła muszą być identyczne.")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Użytkownik z tym adresem email już istnieje.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Użytkownik o tej nazwie już istnieje.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Nazwa użytkownika",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz swoją nazwę użytkownika'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz swoje hasło'}),
        required=True,
        label="Hasło"
    )

class SimplePasswordResetForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email", max_length=150)
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get("username_or_email")
        user = None

        if "@" in username_or_email:  # Jeśli wpisano e-mail
            try:
                user = CustomUser.objects.get(email=username_or_email)
            except CustomUser.DoesNotExist:
                raise forms.ValidationError("No user found with this email.")
        else:  # Jeśli wpisano nazwę użytkownika
            try:
                user = CustomUser.objects.get(username=username_or_email)
            except CustomUser.DoesNotExist:
                raise forms.ValidationError("No user found with this username.")

        cleaned_data["user"] = user
        return cleaned_data