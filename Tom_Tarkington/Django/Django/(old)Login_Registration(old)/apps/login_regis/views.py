from django.shortcuts import render, redirect, reverse
import re, bcrypt


def index(request):
    return render(request, 'login_regis/index.html')

def register(request):
    if request.method == "POST":
        print request.POST
    return redirect(reverse('landing'))

def login(request):
    pass
