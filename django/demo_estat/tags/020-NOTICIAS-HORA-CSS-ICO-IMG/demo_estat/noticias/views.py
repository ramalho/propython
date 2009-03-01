# coding: utf-8

from django.shortcuts import render_to_response
from datetime import datetime

def principal(request):
    vals = {'hora':datetime.now()}
    return render_to_response('noticias/principal.html', vals)
    