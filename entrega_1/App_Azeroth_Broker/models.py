from django.db import models

# Create your models here


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    juego = models.CharField(max_length=30)
    discord = models.CharField(max_length=30)

class Moderador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class juego(models.Model):
    nombre = models.CharField(max_length=30)
    
