# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import string
from django.utils.crypto import get_random_string #for get_random_string

from django.shortcuts import render, redirect

def random_word(n):
    return get_random_string(n)

def index(request):
    try:
        request.session['attempts']
    except KeyError:
        request.session['attempts'] = 0

    return render(request, "randomstring/index.html")

def generate(request):
    request.session['attempts'] += 1  
    request.session['word'] = random_word(10)
    return redirect('/')

def reset(request):
    del request.session['attempts']
    del request.session['word']
    return redirect('/')

