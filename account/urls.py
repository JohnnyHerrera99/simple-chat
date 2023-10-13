from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.RegisterFormView.as_view(), name="register"),
    path("login/", views.LoginWithLogginView.as_view(), name="login"),
    path("logout/", views.LogoutWithLogginView.as_view(), name="logout")
]