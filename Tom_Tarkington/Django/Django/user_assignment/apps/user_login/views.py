# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse

def index(req):
        return HttpResponse("Ready for queries!")

