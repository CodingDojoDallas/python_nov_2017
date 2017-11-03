# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog" 
    return HttpResponse(response)

def create(response):
    return redirect('/')

def show(request, blognumber):
    response = 'placeholder to display blog {}'.format(blognumber)
    return HttpResponse(response)

def edit(request, blognumber):
    response = 'placeholder to edit blog {}'.format(blognumber)
    return HttpResponse(response)

def delete(request, blognumber):
    return redirect('/')


