from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

app_name = "clientes_app"

urlpatterns = [
    path('',views.Home.as_view(), name='home')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#Cargae imagenes

