from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from .forms import MessageForm


class LoginRequiredView(LoginRequiredMixin):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'


class HomePageView(LoginRequiredView, TemplateView):
    template_name = "chat/index.html"


class RoomView(LoginRequiredView, ListView):
    template_name = "chat/room.html"
    context_object_name = "messages"
    model = Message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.request.user.username
        context["room_name"] = self.kwargs.get("room_name")
        context["input_message_form"] = MessageForm
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(room=self.kwargs.get("room_name"))[0:25]
