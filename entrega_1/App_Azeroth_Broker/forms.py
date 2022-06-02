from django import forms

class Vendedor_form(forms.Form):
    nombre= forms.CharField(max_length=30)
    juego = forms.CharField(max_length=30)
    discord = forms.CharField(max_length=30)

class Usuario_form(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class Moderador_form(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


