from dataclasses import fields
from socket import fromshare
from django import forms 
from .models import *

class Personalform(forms.ModelForm):

    class Meta:
        model = Personal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Personalform, self).__init__(*args, **kwargs)
        self.fields['area'].empty_label="Selecciona"
        self.fields['estudios'].empty_label="Selecciona"
        self.fields['carrera'].empty_label="Selecciona"
        self.fields['carrera'].choices =[("","Selecciona"),] + list(self.fields["carrera"].choices)[1:]
        self.fields['ap'].required=True
        #self.fields['am'].required=False
        #Este es el formulario para los campos
