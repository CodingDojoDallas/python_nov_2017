from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from .models import User
from time import localtime, strftime

# Create your views here.
def index(request):
	context = {
	"users": User.objects.all()
	}
	return render(request, 'rest_app/index.html', context)

def show(request, user_id):
	context = {
	"user": (User.objects.get(id=user_id))
	}

	return render(request, 'rest_app/user.html', context)

def new(request):
	return render(request, 'rest_app/new.html')

def edit(request, user_id):
	context = {
	"id": (User.objects.get(id=user_id).id),
	"first_name": (User.objects.get(id=user_id).first_name),
	"last_name": (User.objects.get(id=user_id).last_name),
	"email": (User.objects.get(id=user_id).email)
	}
	return render(request, 'rest_app/edit.html', context)

def create(request):
	User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
	return redirect('/')

def destroy(request, user_id):
	User.objects.get(id=user_id).delete()
	return redirect('/')

def update(request, user_id):

	x = User.objects.get(id=user_id)
	x.first_name = request.POST['first_name']
	x.last_name = request.POST['last_name']
	x.email = request.POST['email']
	x.save()

	return redirect('/')




