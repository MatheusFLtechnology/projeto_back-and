from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def olamundo(request):
   return HttpResponse("<h1>ola mundo</h1>")

def cadastro(request):
   return HttpResponse("cadastro")    
#def contato(request):
   # return render(request, 'contato.html')


