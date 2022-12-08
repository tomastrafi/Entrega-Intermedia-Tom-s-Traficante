from django.http import HttpResponse
import datetime
from django.template import Template, Context
import os.path

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATES_PATH = os.path.join(PROJECT_PATH, 'templates/')

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"


      return HttpResponse(documentoDeTexto)


def probandoTemplate(self):
    nom = 'Tomás'
    ape = 'Traficante'

    diccionario = {
        'nombre': nom,
        'apellido': ape,
        'edades' : [20,60,45,25]
    }

    miHtml = open(TEMPLATES_PATH+"/template1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)