from django.urls import path

from . import views

urlpatterns = [
    path("accounts/register/", views.RegisterFormView.as_view(), name="register")
]