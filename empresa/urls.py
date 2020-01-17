from django.contrib import admin
from django.urls import path, include
from empresa.views import *
urlpatterns = [
    path('cadastro/', mostrar_formulario_cad_empresa),
    path('login/empresa/', login_empresa),
]
