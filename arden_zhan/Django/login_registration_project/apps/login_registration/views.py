# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def login(request):
    result = User.objects.validateLogin(request.POST)
    
    if type(result) == dict:
        for tag, error in result.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')

    request.session['id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def register(request):
    result = User.objects.validateReg(request.POST)
    
    if type(result) == dict:
        for tag, error in result.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    
    request.session['id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def success(request):
    if request.session.get('id') == None:
        return redirect('/')

    context = {
        'user': User.objects.get(id = request.session['id']),
    }
    return render(request, 'login_registration/success.html', context)