from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('room/<str:room_name>/', views.RoomView.as_view(), name='room'),
]