# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    response = {
        "time":strftime("%b %d, %Y %H:%M %p", localtime()),
    }
    return render(request,'time_display/index.html', response)

def time_display(request):
    return redirect('/')
