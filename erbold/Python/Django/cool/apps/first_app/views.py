# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)

def new(request):
	response = "placeholder to display a new form to create a new boogy"
	return HttpResponse(response)

def show(request, number):
	response = number
	return HttpResponse(response)

# def index(request):
# 	response = "Hello, I am your 2nd request!"
# 	return HttpResponse(response)

# Create your views here.
