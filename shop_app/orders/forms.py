from django import forms
from .models import Order
from django.core.exceptions import ValidationError

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'address', 'phone_number', 'payment_method']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) < 9:
            raise ValidationError('Numer telefonu jest za krótki.')
        return phone_number

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order  # lub inny model
        fields = ['address', 'phone_number', 'payment_method']  