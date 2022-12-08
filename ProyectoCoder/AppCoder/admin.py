from django.contrib import admin
from .models import * #importamos el archivo models
admin.site.register(Familia)
admin.site.register(Zona)
admin.site.register(Deporte)