from django.shortcuts import render
from .models import Personal
from .forms import Personalform
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class Inicio(TemplateView):
    template_name = 'paginas_base/inicio.html'
    
class Lista(ListView):
    template_name = 'crud/lista.html'
    model = Personal
    ordering = '-id' # ordenar desendiente
    queryset = Personal.objects.all()
    context_object_name = 'Personas' #obtener el nombre personas
#%$

class Crear(CreateView):
    template_name = 'crud/crear.html'
    model = Personal
    form_class = Personalform

    def get_success_url(self, **kwargs):
        return reverse("personal_app:lista")

class Editar(UpdateView):
    template_name = 'crud/editar.html'#Platilla para el crud 
    model = Personal 
    form_class = Personalform
    pk_url_kwarg= 'pk'

    def get_success_url(self,**kwargs):
        return reverse('personal_app:lista')
    
class Eliminar(DeleteView):#Clase de eliminar por pk
    template_name = "crud/eliminar.html"
    model =Personal
    pk_url_kwarg ='pk' #Elimina mediante le pk

    def get_success_url(self,**kwargs):
        return reverse('personal_app:lista') #Redirigir la aplicacion

