from django.urls import path

from . import views

urlpatterns = [
    path("accounts/register/", views.register_request, name="register")
]