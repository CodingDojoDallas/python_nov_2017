# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
# Create your views here.

def index(request):
    return render(request, 'session_app/index.html')

def add(request):
    if request.method == 'POST':
        form_data = request.POST

        word = {
        'time': strftime("%Y-%m-%d %H:%M %p", gmtime()),
        'word': form_data['word'],
        'color': form_data['color'],
        'bigfont': 'bigfont' if 'bigfont' in form_data else 'smallfont'
        }
        if 'words' not in request.session:
            request.session['words'] = []
        request.session['words'] += [word]

    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')