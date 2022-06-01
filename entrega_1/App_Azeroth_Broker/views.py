from django.shortcuts import render
from django.http import HttpResponse
from . import template
from App_Azeroth_Broker.forms import Vendedor_form
from App_Azeroth_Broker.models import *
from django.template import loader
# Create your views here.


def inicio(request):
    return render(request,"inicio.html")

def vendedor(request):
    vendedor = Vendedor.objects.all()
    dicc = {"vendedores": vendedor}
    plantilla = loader.get_template("vendedores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def juegos(request):
    return render(request,"juegos.html")

def alta_vendedor(request):
    if request.method == "POST":
        mi_formulario = Vendedor_form(request.POST)
        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleaned_data
            vendedor = Vendedor(nombre = datos['nombre'],juego =datos['juego'],discord =datos['discord'])
            vendedor.save()
            return render(request,"vendedores.html")
    return render(request,"form_Vendedor.html")

def buscar_V(request):
    return render(request,"buscar_vendedor.html")
def buscar(request):
    """
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        vendedor = Vendedor.objects.filter(nombre__icontins = nombre)
        return HttpResponse(vendedor)
    else:
        return HttpResponse("Campo Vacio")
    """
    return HttpResponse(f"we are looking for the seller {request.GET['nombre']}")









