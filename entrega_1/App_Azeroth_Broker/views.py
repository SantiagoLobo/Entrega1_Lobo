from django.shortcuts import render
from django.http import HttpResponse
from . import template

# Create your views here.


def inicio(request):
    return render(request,"inicio.html")