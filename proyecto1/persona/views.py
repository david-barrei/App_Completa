from django.shortcuts import render
from .models import Personal

from django.views.generic import TemplateView, ListView

# Create your views here.
class Inicio(TemplateView):
    template_name = 'paginas_base/inicio.html'
    
class Lista(ListView):
    template_name = 'crud/lista'
    model = Personal
    ordering = '-id'
    queryset = Personal.objects.all()
    context_object_name = 'Personas'