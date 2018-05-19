# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(request):
    if request.session.get('results') == None:
        request.session['results'] = []

    return render(request, 'session_words/index.html')

def process(request):
    result = {}

    if 'size' in request.POST:
        result['size'] = request.POST['size']
    else: result['size'] = "normal"

    result['word'] = request.POST['word']
    result['color'] = request.POST['color']
    result['time'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")

    request.session['results'].append(result)
    request.session['results'] = request.session['results']

    return redirect('/')

def clear(request):
    request.session['results'] = []
    return redirect('/')

