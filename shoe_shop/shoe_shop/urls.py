"""
URL configuration for Weiboo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from shoe_shop import homeViews
from shop import views as shopViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('', homeViews.index, name ='index'),
    path('all-category', homeViews.allCategory, name='allCategory'),
    path('category', homeViews.category, name='category'),
    path('external-products', homeViews.externalProducts, name='externalProducts'),
    path('index', homeViews.index, name='index'),
    path('index-two', homeViews.indexTwo, name='indexTwo'),
    path('login', homeViews.login, name='login'),
    path('out-of-stock-products', homeViews.outOfStockProducts, name='outOfStockProducts'),
    path('shop-five-column', homeViews.shopFiveColumn, name='shopFiveColumn'),
    path('simple-products', homeViews.simpleProducts, name='simpleProducts'),
    path('thankYou', homeViews.thankYou, name='thankYou'),
    path('wishlist', homeViews.wishlist, name='wishlist'),

    # shop

    path('check-out', shopViews.checkOut, name='checkOut'),
    path('full-width-shop', shopViews.fullWidthShop, name='fullWidthShop'),
    path('grouped-products', shopViews.groupedProducts, name='groupedProducts'),
    path('product-details', shopViews.productDetails, name='productDetails'),
    path('shop', shopViews.shop, name='shop'),
    path('sidebar-left', shopViews.sidebarLeft, name='sidebarLeft'),
    path('sidebar-right', shopViews.sidebarRight, name='sidebarRight'),
    path('variable-products', shopViews.variableProducts, name='variableProducts'),

    # cart
    path('cart/', include('cart.urls')),
    # users
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)