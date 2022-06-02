from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio),
    path("vendedores/", views.vendedor, name="vendedores"),
    path("juegos/", views.juegos, name="juegos"),
    path("alta", views.alta_vendedor, name="alta_vendedor"),
    path("buscar_v",views.buscar_v, name="buscar_v"),
    path("buscar",views.buscar, name="buscar"),
    path("mods/",views.mods, name="mods"),
    path("usuario/",views.usuario, name="usuario"),
    path("alta_m",views.alta_mod, name="alta_moderador"),
    path("alta_u",views.alta_usuario,name="alta_usuario")
]