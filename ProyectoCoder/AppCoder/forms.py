from django import forms

class FamiliaFormulario(forms.Form):
    nombre= forms.CharField(max_length=40)
    rol= forms.CharField(max_length=40)
    trabajo= forms.CharField(max_length=40)
    edad= forms.IntegerField()

class ZonaFormulario(forms.Form):
    provincia=forms.CharField(max_length=40)
    ciudad=forms.CharField(max_length=40)
    barrio=forms.CharField(max_length=40)
    codigo_postal=forms.IntegerField()

class DeporteFormulario(forms.Form):
    deporte_favorito=forms.CharField(max_length=40)
    club=forms.CharField(max_length=40)
    posicion=forms.CharField(max_length=40)
    años_jugando=forms.IntegerField()