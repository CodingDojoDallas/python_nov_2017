from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = 'Placeholder to later display all the list of blogs'
	return HttpResponse(response)

def new(request):
	response = 'placeholder to display a form to create a new blog'
	return HttpResponse(response)

def create(request):
	
	return redirect('/')

def show(request, blog_id):
	response = 'placeholder to display blog {{blog_id}}'
	return HttpResponse(response)

def edit(request, blog_id):
	response = 'placeholder to edit blog {{blog_id}}'
	return HttpResponse(response)

def destroy(request):
	
	return redirect('/')








# Create your views here.
