# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    try: 
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0

    return render(request, 'random_word/index.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')

def generate(request):
    request.session['randomword'] = get_random_string(length=14)
    request.session['counter'] += 1
    return redirect('/random_word')
    
    