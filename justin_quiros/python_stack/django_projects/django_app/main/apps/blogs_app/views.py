from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'blogs_app/index.html')

def new(request):
	return render(request, 'blogs_app/new.html')

def create(request):
	return render(request, 'blogs_app/index.html')

def show(request, number):
	return HttpResponse("Placeholder to display blog " + number)

def edit(request, number):
	return HttpResponse("Placeholder to edit blog " + number)

def destroy(request, number):
	return render(request, 'blogs_app/index.html')
