from django.urls import path
from . import views

app_name = "personal_app"


urlpatterns = [
    path('',views.Inicio.as_view(), name='inicio'),
    path('lista/',views.Lista.as_view(), name='lista'),
    path('crear/',views.Crear.as_view(), name='crear'),
    path('editar/<pk>',views.Editar.as_view(), name='editar'),#Id por parametro
    path('eliminar/<pk>',views.Eliminar.as_view(), name='eliminar'),#Pasar por parametro el id 
    
]#urls 