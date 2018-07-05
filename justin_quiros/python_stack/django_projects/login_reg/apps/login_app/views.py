from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
	request.session['status'] = ""
	if 'errors' not in request.session:
		request.session['errors'] = []
	context = {
	"errors": request.session['errors']
	}
	return render(request, 'login_app/index.html', context)

def register(request):
	if request.method == "POST":
		errors = User.objects.register_validation(request.POST)
		if len(errors) != 0:
			request.session['errors'] = errors
			print errors
			return redirect('/')
		else:
			user = User.objects.register(request.POST)
			request.session['user_id'] = user.id
			request.session['status'] = "registered."
			request.session['name'] = user.first_name
			return redirect('/success')

def login(request):
	errors = User.objects.login_validation(request.POST)
	if len(errors) != 0:
		request.session['errors'] = errors
		return redirect('/')
	else:
		user = User.objects.login(request.POST)
		request.session['name'] = user.first_name
		request.session['status'] = "logged in."
		return render(request, 'login_app/success.html')

def success(request):
	return render(request, 'login_app/success.html')

def logout(request):
	request.session.clear()
	return redirect('/')