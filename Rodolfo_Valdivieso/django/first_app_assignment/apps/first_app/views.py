# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
# Create your views here.
def index(request):
	#return render(request, 'index.html')
	response = "Hello, I am your first Request!!!!!!!! YESSSSS Moving forward...."
	return HttpResponse(response)

def new(request):
#return render(request, 'index.html')
	response = "Your URL is just /new...."
	return HttpResponse(response)

def create(request):
#return render(request, 'index.html')
	response = "Your URL is just /Create...."
	return HttpResponse(response)

def show(request, number):
#return render(request, 'index.html')
	return HttpResponse("Your URL is just /Show2..  " + number)

def edit(request, number):
#return render(request, 'index.html')
	return HttpResponse("Your URL is just Edit.  " + number)

def destroy(request, number):
#return render(request, 'index.html')
	return HttpResponse("Your URL is just Destroy  " + number)