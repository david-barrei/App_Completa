from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.views.generic import TemplateView


# Create your views here.

class Home(TemplateView):
    template_name='crud/home.html'

class compras(TemplateView):
    template_name='crud/compras.html'
