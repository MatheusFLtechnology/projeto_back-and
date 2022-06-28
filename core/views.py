from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 
def home(request):
    return render(request, 'index.html',{'nome':'IFRN'})


def olamundo(request):
   return HttpResponse("<h1>ola mundo</h1>")

def cadastro(request):
    return render(request, 'cadastro.html',{'nome':'cadastro'})

def masculino(request):
    return render(request, 'masculino.html',{'nome':'masculino'})

   


