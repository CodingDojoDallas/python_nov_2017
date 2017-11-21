# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
  # the index function is called when root is visited
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    response = "The Time and Date is:"
    return HttpResponse(response)

def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
  return render(request,'timeDisp_app/index.html', context)