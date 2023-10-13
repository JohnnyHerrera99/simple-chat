from django.shortcuts import  render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import NewUserForm
import datetime
import logging

logger = logging.getLogger(__name__)


class RegisterFormView(FormView):
	template_name = "register.html"
	form_class = NewUserForm
	success_url = "/"

	def dispatch(self, request, *args, **kwargs):
		logger.warning(f'[{datetime.datetime.now()}] Register was accessed - user {request.user}')
		return super().dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		logger.warning(f'[{datetime.datetime.now()}] Register and login new user {user}')
		return super().form_valid(form)


class LoginWithLogginView(LoginView):

	def dispatch(self, request, *args, **kwargs):
		logger.warning(f'[{datetime.datetime.now()}] Login was accessed - user {request.user}')
		return super().dispatch(request, *args, **kwargs)

class LogoutWithLogginView(LogoutView):
	def dispatch(self, request, *args, **kwargs):
		logger.warning(f'[{datetime.datetime.now()}] Logout - user {request.user}')
		return super().dispatch(request, *args, **kwargs)
