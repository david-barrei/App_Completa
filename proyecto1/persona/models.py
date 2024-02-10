from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Para saber cual es el usuario hizo el cambio
# Create your models here.

class Area(models.Model):
    nom_Area=models.CharField(max_length=100, verbose_name ='Area', null= False, blank=False)

    def __str__(self):
        fila = self.nom_Area
        return fila
    
class Estudios(models.Model):
    nom_Estudios=models.CharField( max_length=100, blank=False, null = False)

    def __str__(self):
        fila = self.nom_Estudios
        return fila

carrera = (
    ('sistemas','sistemas')
    ('TICs','TICs')
    ('Sofware','Sofware')
    ('Ciencias de la computacion','Ciencias de la computacion')
    ('Programador','Programador')
)