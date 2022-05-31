from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio),
    path("vendedores/", views.vendedor, name="vendedores"),
    path("contacto/", views.contacto),
    path("juegos/", views.juegos, name="juegos")
]