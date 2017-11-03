from django.shortcuts import render, redirect, reverse

def index(request):

    return render(request, 'user_login/index.html')
