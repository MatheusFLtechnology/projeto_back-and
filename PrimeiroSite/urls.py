"""PrimeiroSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from core.views import  home, cadastro, masculino, feminina, criancas, compra


urlpatterns = [
  # path('ola/', olamundo),
   path('', home),
   path('register/',cadastro,name='cadastro'),
   path('man/',masculino,name='masculino'),
   path('female/',feminina,name='feminina'),
   path('kids/',criancas, name='criancas'),
   path('compra/',compra, name='compra'),


    
    #path('contato/',contato, name="contato"),
    path('admin/', admin.site.urls),
]
