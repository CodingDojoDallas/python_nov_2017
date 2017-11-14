from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
def index(request):
	if request.session.get('name') == None:
		request.session['name'] = ""

	if request.session.get('location') == None:
		request.session['location'] = ""

	if request.session.get('language') == None:
		request.session['language'] = ""

	if request.session.get('comments') == None:
		request.session['comments'] = ""

	if request.session.get('attempts') == None:
		request.session['attempts'] = 0


	return render(request, 'survey_app/index.html')

def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comments'] = request.POST['comments']
	return redirect('/result')

def result(request):
	request.session['attempts'] += 1
	return render(request, 'survey_app/result.html')