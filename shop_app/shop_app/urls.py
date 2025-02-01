"""
URL configuration for shop_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from users import views as user_views 

from django.views.generic import TemplateView  # Zaimportuj TemplateView

urlpatterns = [
    path('', user_views.login_view, name='home'),  # Strona główna to teraz logowanie
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),  # Strona z produktami
    path('users/', include('users.urls')),  # Strona z użytkownikami (logowanie, rejestracja)
    
    # Strony logowania i rejestracji
    path('accounts/login/', user_views.login_view, name='login'),
    path('accounts/logout/', user_views.logout_view, name='logout'),
    path('accounts/register/', user_views.register_view, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)