# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
	if (request.session.get('gold') == None):
		request.session['gold'] = 0 
	if (request.session.get('activities') == None):
		request.session['activities'] = []
	if (request.session.get('building') == None):
		request.session['building'] = ""
	return render(request, 'first_app/index.html')

def process_money(request):
	building = request.session['building']
	goldEarned = 0
	activity   = ""
	if building == "farm":
		goldEarned = random.randint(10, 20)
	elif building == "cave":
		goldEarned = random.randint(5, 10)
	elif building == "house":
		goldEarned = random.randint(2, 5)
	elif building == "casino":
		goldEarned = random.randint(-50, 50)

	if goldEarned >= 0:
		activity = "Earned: " + str(goldEarned) + " Golds from the " + building + "! (" + str(datetime.datetime.now()) +")"
		color = "green"
	else:
		activity = "Enter a Casino  and Lost: " + str(goldEarned) + " ..Ouch... "  + " (" + str(datetime.datetime.now())+")"
		color = "red"

	dictionary = {"record":activity, "class":color}
	temp = request.session.get('activities')
	temp.append(dictionary)
	request.session['activities'] = temp
	request.session['gold'] = int(request.session.get('gold')) + goldEarned


	if int(request.session.get('gold')) < 0:
		request.session['gold'] = 0

	return redirect('/')


def farm(request):
	request.session['building'] = "farm"
	return process_money(request)

def cave(request):
	request.session['building'] = "cave"
	return process_money(request)

def house(request):
	request.session['building'] = "house"
	return process_money(request)

def casino(request):
	request.session['building'] = "casino"
	return process_money(request)

def reset(request):
	del request.session['gold']
	del request.session['activities']
	del request.session['building']
	return redirect('/')
