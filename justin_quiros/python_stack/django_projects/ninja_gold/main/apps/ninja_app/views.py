from django.shortcuts import render, redirect
from random import random, randint
from time import localtime, strftime

# Create your views here.
def index(request):

	if request.session.get('gold') == None:
		request.session['gold'] = 0
	if request.session.get('farm') == None:
		request.session['farm'] = 0
	if request.session.get('cave') == None:
		request.session['cave'] = 0
	if request.session.get('house') == None:
		request.session['house'] = 0
	if request.session.get('casino') == None:
		request.session['casino'] = 0
	if request.session.get('x') == None:
		request.session['x'] = ""
	if request.session.get('activity') == None:
		request.session['activity'] = []

	return render(request, 'ninja_app/index.html')

def process(request):

	if request.POST['action'] == 'farm':
		request.session['farm'] = randint(10,21)
		request.session['gold'] += request.session['farm']
		x = "Earned {} golds from the {}! ({})".format(request.session['farm'], request.POST['action'], strftime("%I:%M %p, %b-%d-%Y", localtime()))
		color = "green"

	if request.POST['action'] == 'cave':
		request.session['cave'] = randint(5,11)
		request.session['gold'] += request.session['cave']
		x = "Earned {} golds from the {}! ({})".format(request.session['cave'], request.POST['action'], strftime("%I:%M %p, %b-%d-%Y", localtime()))
		color = "green"

	if request.POST['action'] == 'house':
		request.session['house'] = randint(2,6)
		request.session['gold'] += request.session['house']
		x = "Earned {} golds from the {}! ({})".format(request.session['house'], request.POST['action'], strftime("%I:%M %p, %b-%d-%Y", localtime()))
		color = "green"

	if request.POST['action'] == 'casino':
		request.session['casino'] = randint(-51,51)
		if int(request.session['casino']) >= 0:
			x = "Earned {} golds from the {}! ({})".format(request.session['casino'], request.POST['action'], strftime("%I:%M %p, %b-%d-%Y", localtime()))
			color = "green"
		else:
			x = "Entered a {} and lost {} golds... Ouch... ({})".format(request.POST['action'], request.session['casino'], strftime("%I:%M %p, %b-%d-%Y", localtime()))
			color = "red"
			request.session['gold'] += request.session['casino']


	activity = {
		"color": color,
		"activity": x
	}

	temp = request.session['activity']
	temp.append(activity)
	request.session['activity'] = temp

	return redirect('/')

def again(request):
	del request.session['gold']
	del request.session['activity']
	return	redirect('/')