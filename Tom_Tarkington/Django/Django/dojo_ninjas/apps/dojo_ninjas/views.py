from django.shortcuts import render, redirect, reverse

def index(request):

    return render(request, 'dojo_ninjas/index.html')
