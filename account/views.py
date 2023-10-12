from django.shortcuts import  render, redirect
from django.views.generic.edit import FormView

from .forms import NewUserForm
from django.contrib.auth import login


class RegisterFormView(FormView):
    template_name = "register.html"
    form_class = NewUserForm
    success_url = "/"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def register_request(request):
	context = {}
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/")
		
		errors = form.errors
		if "password2" in errors:
			errors["password confirmation"] = errors["password2"]
			del errors["password2"]
		context["error"] = errors
	form = NewUserForm()
	context["register_form"] = form
	return render (request=request, template_name="register.html", context=context)