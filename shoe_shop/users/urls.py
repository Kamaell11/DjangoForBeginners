from django.urls import path
from .views import register_view, login_view, logout_view, simple_password_reset_view, account_view

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("password_reset/", simple_password_reset_view, name="password_reset"),
    path("account/", account_view, name="account"),
]