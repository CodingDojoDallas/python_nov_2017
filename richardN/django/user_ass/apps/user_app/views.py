# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
# the index function is called when root is visited
def index(request):
    return HttpResponse("Shell Queries")