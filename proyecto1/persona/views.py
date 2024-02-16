from django.shortcuts import render
from .models import *

from django.views.generic import TemplateView

# Create your views here.
class Inicio(TemplateView):
    template_name = 'paginas_base/inicio.html'
    