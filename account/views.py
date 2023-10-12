from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login

def register_request(request):
	context = {}
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/")
		print(form.errors)
		context["error"] = form.errors
	form = NewUserForm()
	context["register_form"] = form
	return render (request=request, template_name="register.html", context=context)