# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# locations/money list in locations.py
from locations import locations
from random import randint
from datetime import datetime

# Create your views here.
def index(request):
    if request.session.get('total_gold') == None:
        request.session['total_gold'] = 0
    
    context = {
        'locations': locations
    }

    return render(request, "ninja_gold/index.html", context)

def process(request, location_name):
    result = {}

    for location in locations:
        if location['name'] == location_name.capitalize():
            gold_change = randint(location['low'], location['high'])
            result['location_name'] = location_name
            result['gold_change'] = gold_change
            result['time'] = datetime.now().strftime("%I:%M %p, %B %d, %Y")
            break

    if request.session.get('activities') == None:
        request.session['activities'] = []

    request.session['activities'].append(result)
    request.session['activities'] = request.session['activities']

    request.session['total_gold'] += gold_change
    
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')

