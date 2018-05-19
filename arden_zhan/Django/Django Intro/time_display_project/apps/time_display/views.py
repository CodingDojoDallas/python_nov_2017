# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import strftime

def index(request):
    context = {
        # by default, strftime('%format', localtime()) //localtime is used default
        'date': strftime('%b %d, %Y'),
        'time': strftime('%I:%M %p')
    }
    return render(request, "time_display/index.html", context)
