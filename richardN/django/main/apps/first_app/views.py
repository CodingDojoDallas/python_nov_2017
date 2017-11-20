# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Oh where oh where can my baby be?"
    return HttpResponse(response)
