from django.shortcuts import render
from .models import Personal
from .forms import Personalform
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, ListView, CreateView

# Create your views here.
class Inicio(TemplateView):
    template_name = 'paginas_base/inicio.html'
    
class Lista(ListView):
    template_name = 'crud/lista.html'
    model = Personal
    ordering = '-id'
    queryset = Personal.objects.all()
    context_object_name = 'Personas'

class Crear(CreateView):
    template_name = 'crud/crear.html'
    model = Personal
    form_class = Personalform

    def get_success_url(self, **kwargs):
        return reverse("personal_app:lista")