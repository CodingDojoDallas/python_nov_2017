from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Hello, I am your first request!"
	return HttpResponse(response)

def test(request):
	response = "Hello I am a test"
	return HttpResponse(response)

# Create your views here.
a