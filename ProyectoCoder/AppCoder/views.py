from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Familia
from AppCoder.models import Zona
from AppCoder.models import Deporte
from django.core import serializers

from AppCoder.forms import FamiliaFormulario
from AppCoder.forms import ZonaFormulario
from AppCoder.forms import DeporteFormulario

# Create your views here.
def inicio(request):
    return render(request,'AppCoder/Inicio.html')

def familia(request):
    if request.method == "POST":
            miFormulario = FamiliaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                familia = Familia(nombre=informacion["nombre"], rol=informacion["rol"], trabajo=informacion['trabajo'], edad=informacion["edad"])
                familia.save()
                return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = FamiliaFormulario()
        
    return render(request, 'AppCoder/familia.html', {'miFormulario': miFormulario})

def zona(request):
    if request.method == "POST":
            miFormulario = ZonaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                zona = Zona(provincia=informacion["provincia"], ciudad=informacion["ciudad"], barrio=informacion['barrio'], codigo_postal=informacion["codigo_postal"])
                zona.save()
                return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ZonaFormulario()
        
    return render(request, 'AppCoder/zona.html', {'miFormulario': miFormulario})

def deporte(request):
    if request.method == "POST":
            miFormulario = DeporteFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                deporte = Deporte(deporte_favorito=informacion["deporte_favorito"], club=informacion["club"], posicion=informacion['posicion'], años_jugando=informacion["años_jugando"])
                deporte.save()
                return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = DeporteFormulario()
        
    return render(request, 'AppCoder/deporte.html', {'miFormulario': miFormulario})

def familiaapi(request):
    familias_todos = Familia.objects.all()
    return HttpResponse(serializers.serialize('json',familias_todos))

def zonaapi(request):
    zonas_todas = Zona.objects.all()
    return HttpResponse(serializers.serialize('json',zonas_todas))

def deporteapi(request):
    deportes_todos = Deporte.objects.all()
    return HttpResponse(serializers.serialize('json',deportes_todos))