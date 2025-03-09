from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('product/<int:shoe_id>/', views.product_details, name='productDetails'),
    path('featured/', views.featured_shoes, name='featured_products'),
    
]