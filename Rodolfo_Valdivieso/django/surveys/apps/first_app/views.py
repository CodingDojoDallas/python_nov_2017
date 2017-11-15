# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
  if (request.session.get('name') == None):
  	request.session['name'] = ""
  if request.session.get('location') == None:
  	request.session['location'] = ""
  if request.session.get('language') == None:
  	request.session['language'] = ""
  if request.session.get('comment') == None:
  	request.session['comment'] = ""
  if request.session.get('attempts') == None:
  	request.session['attempts'] = 0

  return render(request, 'first_app/index.html')


def create(request):

  first_name = request.POST['firstName']
  location = request.POST['location']
  language = request.POST['language']
  comment = request.POST['comment']

  request.session['name'] = first_name
  request.session['location'] = location
  request.session['language'] = language
  request.session['comment'] = comment
  
  error = 0
  if len(first_name) < 1 :
  	messages.error(request, "Name cannot be empty!")
  	error = 1
  if location=="":
  	messages.error(request, "You must pick a Location!")
  	error = 1
  if language=="":
  	messages.error(request, "You must chosse a language!")
  	error = 1
  if len(comment) < 1:
  	messages.error(request, "Comment cannot be empty!")
  	error = 1
  if len(comment) > 10:
  	messages.error(request, "Comment cannot be more than 10 characters!")
  	error = 1

  if error != 0:
	return redirect('/')
  else:
  	request.session['attempts'] = int(request.session['attempts'])+1
  	#messages.success(request, "this is my success message")
  	return redirect('/result') 

def result(request):
  return render(request, 'first_app/result.html')

def goback(request):
  request.session['name'] = ""
  request.session['location'] = ""
  request.session['language'] = ""
  request.session['comment'] = ""
  return redirect('/')  