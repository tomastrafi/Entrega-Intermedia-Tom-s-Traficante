from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('familia/', views.familia,name='Familia'),
    path('familiaApi/', views.familiaapi,),
    path('zona/', views.zona,name='Zona'),
    path('zonaApi/', views.zonaapi),
    path('deporte/', views.deporte,name='Deporte'),
    path('busquedaFamilia/', views.buscarfamilia),
    path('buscar/', views.buscar),
    path('deporteApi/', views.deporteapi)]