# products/admin.py
from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('price', 'created_at')

admin.site.register(Product, ProductAdmin)
