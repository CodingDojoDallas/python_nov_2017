# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
	if (request.session.get('word')==None):
		request.session['word'] = ""
	if (request.session.get('history')==None):
		request.session['history'] = []
	return render(request, 'first_app/index.html')

def addWord(request):
	message = "added on " + strftime("%H:%M %p", gmtime()) +", "+ strftime("%b %d, %Y", gmtime())
	request.session['word'] = request.POST.get('word')
	if request.POST.get('font') == None:
		font = ""
	else:
		font = request.POST.get('font')
	dictionary = {
		"word":request.POST.get('word'),
		"class":request.POST.get('color'),
		"font":font,
		"message":message
	}
	request.session['history'].append(dictionary)
	return redirect('/')

def clearWord(request):
	del request.session['word']
	del request.session['history']
	return redirect('/')