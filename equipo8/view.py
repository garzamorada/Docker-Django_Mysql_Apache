from django.http import HttpRequest
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def prueba(request):
    return render(request,'prueba.html')
    