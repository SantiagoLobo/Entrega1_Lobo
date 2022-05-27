from django.db import models

# Create your models here


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidade = models.CharField(max_length=30)
    email = models.EmailField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    Server = models.CharField(max_length=30)
    stock = models.IntegerField()
    precio = models.FloatField()
    

class Moderador(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField()


