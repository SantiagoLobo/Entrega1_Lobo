from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio),
    path("vendedores/", views.vendedor, name="vendedores"),
    path("juegos/", views.juegos, name="juegos"),
    path("alta", views.alta_vendedor, name="alta_vendedor"),
    path("vendedor_search/",views.buscar_V,name="buscar_v"),
    path("buscar/",views.buscar)
]