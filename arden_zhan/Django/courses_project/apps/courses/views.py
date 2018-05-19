# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Course, Desc
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'courses/index.html', context)

def create(request):
    course_errors = Course.objects.validate(request.POST)
    desc_errors = Desc.objects.validate(request.POST)
    
    if len(course_errors) or len(desc_errors):
        for tag, error in course_errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        for tag, error in desc_errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    
    c = Course.objects.create(
        name = request.POST['name']
    )

    Desc.objects.create(
        content = request.POST['desc'],
        course = c,
    )

    return redirect('/')

def destroy(request, id):
    Course.objects.get(id = id).delete()
    return redirect('/')