from django.shortcuts import render
from django.http import HttpResponse
from . import template
from App_Azeroth_Broker.forms import *
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

def mods(request):
    mod = Moderador.objects.all()
    dicc = {"mods": mod}
    plantilla = loader.get_template("Mods.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def usuario(request):
    user = Usuario.objects.all()
    dicci = {"usuarios": user}
    plantillas = loader.get_template("Usuario.html")
    documento = plantillas.render(dicci)
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

def alta_usuario(request):
    if request.method == "POST":
        mi_formulario = Usuario_form(request.POST)
        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleaned_data
            usuario = Usuario(nombre = datos['nombre'],apellido =datos['apellido'],email =datos['email'])
            usuario.save()
            return render(request,"Usuario.html")
    return render(request,"form_Usuario.html")

def alta_mod(request):
    if request.method == "POST":
        mi_formulario = Moderador_form(request.POST)
        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleaned_data
            mod = Moderador(nombre = datos['nombre'],apellido =datos['apellido'],email =datos['email'])
            mod.save()
            return render(request,"Mods.html")
    return render(request,"form_Moderador.html")

def buscar_v(request):
    return render(request,"buscar_vendedor.html")


def buscar(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        vendedor = Vendedor.objects.filter(nombre__icontains = nombre)
        return render(request,"resultado_busqueda.html",{"vendedor": vendedor})
    else:
        return HttpResponse("Campo Vacio")
    
    
    
    
    #return HttpResponse(f"we are looking for the seller {request.GET['nombre']}")
    

