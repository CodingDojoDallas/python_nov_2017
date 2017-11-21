# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1

    content = {
        'random': get_random_string(length=14)
    }
    return render(request, 'randomWg_app/index.html', content)

def reset(request):
    del request.session['count']
    return redirect(index)