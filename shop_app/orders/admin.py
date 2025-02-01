from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    # Customize list_display to reflect the actual fields
    list_display = ['id', 'get_customer', 'get_total_price', 'ordered_at']
    
    # Method to get the username of the user (customer)
    def get_customer(self, obj):
        return obj.user.username  # Accessing the username of the related User model
    get_customer.admin_order_field = 'user'  # This will allow sorting by the user
    
    # Method to calculate the total price (assuming product has a price field)
    def get_total_price(self, obj):
        return obj.product.price * obj.quantity  # Multiply product price by quantity
    get_total_price.admin_order_field = 'total_price'  # Allow sorting by total price
    
    # You can also use the 'ordered_at' directly
    def ordered_at(self, obj):
        return obj.ordered_at
    ordered_at.admin_order_field = 'ordered_at'  # Allow sorting by ordered_at

    # Filter by ordered_at field
    list_filter = ['ordered_at']