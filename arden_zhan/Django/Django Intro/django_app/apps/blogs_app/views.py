# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    # response = "placeholder to later display all the list of blogs"
    # return HttpResponse(response)
    context = {
        "email": "arden@arden.com",
        "name": "arden"
    }
    return render(request, "blogs_app/index.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print "*"*50
        return redirect('/blogs')
    else:
        return redirect('/blogs')

def show(request, number):
    response = "placeholder to display blog {}".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog {}".format(number)
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/blogs')