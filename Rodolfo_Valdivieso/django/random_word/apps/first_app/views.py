# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

  if request.session['attempt'] == None:
  	request.session['attempt'] = 1
  else:
  	request.session['attempt'] = int(request.session['attempt']) + 1
  word = get_random_string(length=14, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  context = {
  		"word":word, 
  		"attempt":request.session['attempt']
  }

  return render(request, 'first_app/index.html', context)


def clean(request):
  request.session['attempt'] = 0
  return redirect('/')

def generate(request):
  return redirect('/')
