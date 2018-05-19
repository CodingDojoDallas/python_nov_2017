# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.session.get('total') == None:
        request.session['total'] = 0
    if request.session.get('count') == None:
        request.session['count'] = 0

    # check to remove current_total if go to checkout immediately
    if request.session.get('current_total') != None:
        del request.session['current_total']

    return render(request, "amadon/index.html")

def checkout(request):
    return render(request, "amadon/checkout.html")

def process(request):
    if request.method != 'POST':
        return redirect('/amadon')
        
    quantity = int(request.POST['quantity'])
    product_id = int(request.POST['product_id'])

    if product_id == 101:
        request.session['current_total'] = (quantity * 19.99)
    elif product_id == 102:
        request.session['current_total'] = (quantity * 29.99)
    elif product_id == 103:
        request.session['current_total'] = (quantity * 4.99)
    elif product_id == 104:
        request.session['current_total'] = (quantity * 49.99)
    
    current_total = request.session['current_total']
    request.session['count'] += quantity
    request.session['total'] += current_total

    return redirect('/amadon/checkout')
