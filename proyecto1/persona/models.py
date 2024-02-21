from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Para saber cual es el usuario hizo el cambio
# Create your models here.
from clientes.models import DatosBase

class Area(DatosBase):
    nom_Area=models.CharField(max_length=100, verbose_name ='Area', null= False, blank=False)
    

    def __str__(self):
        fila = self.nom_Area
        return fila
    
class Estudios(DatosBase):
    nom_Estudios=models.CharField( max_length=100, blank=False, null = False)

    def __str__(self):
        fila = self.nom_Estudios
        return fila

carrera = (  #Choices para escojer el tipo de carrera
    ('sistemas','sistemas'),
    ('TICs','TICs'),
    ('Sofware','Sofware'),
    ('Ciencias de la computacion','Ciencias de la computacion'),
    ('Programador','Programador')
)

class Personal(DatosBase):#Extiende
    nom = models.CharField(max_length=50, verbose_name='Nombre', blank= False, null= False)
    ap = models.CharField(max_length=50, verbose_name='Apellido Materno', blank= False, null= False)
    am = models.CharField(max_length=50, verbose_name='Apellido Paterno', blank= False, null= False)
    foto = models.ImageField(upload_to='imagenes/', verbose_name='Foto',blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='Area', on_delete= models.CASCADE)
    estudios = models.ForeignKey(Estudios, verbose_name='Estudios', on_delete= models.CASCADE)
    carrera = models.CharField(max_length=30,verbose_name='Carrera',choices=carrera)

    def __str__(self):
        fila = str(self.id) + '-' + self.nom + '-' + self.ap
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()
    
#Agregando Modelos
