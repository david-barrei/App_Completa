from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class DatosBase(models.Model):
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    usuario = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE) #Este usuario es creado por django


    class Meta:
        abstract =True
        