from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render (request,'surveyform/index.html')

def success(request):
    
    return render(request,'surveyform/success.html')
