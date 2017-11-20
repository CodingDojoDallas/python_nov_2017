from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):

	if request.session.get('attempt') == None:
		request.session['attempt'] = 1
	else:
		request.session['attempt'] += 1
	
	request.session['rand'] = get_random_string(length=14, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	
	return render(request, 'word_gen/index.html')

def generator(request):
	return redirect('/')

def reset(request):
	request.session['attempt'] = 0
	return redirect('/')
	


