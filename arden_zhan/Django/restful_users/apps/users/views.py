# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import User
from django.contrib import messages

# Create your views here.

# TEMPLATES
def index(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/new.html')

def edit(request, id):
    context = {
        'user': User.objects.get(id = id),
    }
    return render(request, 'users/edit.html', context)

def show(request, id):
    context = {
        'user': User.objects.get(id = id),
    }
    return render(request, 'users/show.html', context)


# no template
def destroy(request, id):
    User.objects.get(id = id).delete()
    return redirect('/users')


# POST METHODS
def create(request):
    errors = User.objects.validate(request.POST)
    
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect(reverse('new'))
    
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
    )
    return redirect(reverse('index'))

def update(request, id):
    errors = User.objects.validate(request.POST)
    
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/users/{}/edit'.format(id))
    
    user = User.objects.get(id = id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/{}'.format(id))