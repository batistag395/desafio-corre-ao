"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuario.views import mostrar_pessoas, mostrar_formulario_cadastro
from empresa.views import mostrar_empresas, mostrar_formulario_cad_empresa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mostrar_formulario_cadastro),
    path('pessoas/', mostrar_pessoas),
    path('empresas/', mostrar_empresas),
    path('cad-empresa', mostrar_formulario_cad_empresa)

]
