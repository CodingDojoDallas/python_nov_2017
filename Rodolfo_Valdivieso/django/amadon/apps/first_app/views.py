# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	request.session['products'] = [
		{"id":"0","item":"Dojo Tshirt"   , "price":"19.99"},
		{"id":"1","item":"Dojo Sweater"  , "price":"29.99"},
		{"id":"2","item":"Dojo Cup"      , "price":"4.99"},
		{"id":"3","item":"Algorithm Book", "price":"49.99"}
	]

	request.session['price_list'] =[19.99, 29.99, 4.99, 49.99]

	if request.session.get('amount_charged') == None:
		request.session['amount_charged'] = 0
	if request.session.get('amount_spent') == None:
		request.session['amount_spent']   = 0
	if request.session.get('items') == None:
		request.session['items']          = 0
	
	return render(request, 'first_app/index.html')

def buy(request):
	price_list = request.session.get('price_list')
	i = int(request.POST['price'])
	price = float(price_list[i])
	request.session['amount_charged'] = price* float(request.POST['quantity'])
	request.session['amount_spent']   = float(request.session.get('amount_spent')) + (price* float(request.POST['quantity']))
	request.session['items']          = int(request.session.get('items')) + int(request.POST['quantity'])
	return redirect('/amadon/checkout')


def checkout(request):
	return render(request, 'first_app/checkout.html')

def goback(request):
	return redirect('/')

def clearsession(request):
	del request.session['amount_charged']
	del request.session['amount_spent']
	del request.session['items']
	return redirect('/')