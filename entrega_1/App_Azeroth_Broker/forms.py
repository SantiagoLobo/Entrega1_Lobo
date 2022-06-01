from django import forms

class Vendedor_form(forms.Form):
    nombre= forms.CharField(max_length=30)
    juego = forms.CharField(max_length=30)
    discord = forms.CharField(max_length=30)

