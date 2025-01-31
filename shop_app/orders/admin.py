from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'order_date')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'product__name')

    def user(self, obj):
        return obj.user.username  # You can replace 'username' with other fields if needed

admin.site.register(Order, OrderAdmin)
