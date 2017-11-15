from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
	context = {
	"time": strftime("%b-%d-%Y %I:%M %p", localtime())
	}

	return render(request,'index.html', context)
