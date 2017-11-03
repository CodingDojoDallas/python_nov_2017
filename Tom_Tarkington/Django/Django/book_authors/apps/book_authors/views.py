from django.shortcuts import render, redirect, reverse

def index(request):
    return render(request, 'book_authors/index.html')
