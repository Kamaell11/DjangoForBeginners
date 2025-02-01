from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'status']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order  # lub inny model
        fields = ['address', 'phone_number', 'payment_method']  