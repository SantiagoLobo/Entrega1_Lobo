from django.shortcuts import render
from django.http import HttpResponse
from . import template

# Create your views here.


def inicio(request):
    return render(request,"inicio.html")

def vendedor(request):
    return render(request,"vendedores.html") 

def contacto(request):
    return render(request,"contacto.html")

def juegos(request):
    return render(request,"juegos.html")