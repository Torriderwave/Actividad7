"""colegioA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Apps.home import views
from .views import HomeView,EstudianteView,AdminView,AcercaView,CrearPublicacionView,CrearComentarioView,CrearArticuloView,CrearAutorizacionView,ListarEstudianteView,ListarAutorizacionView,ListarArticuloView,ComentarioView,ListarComentarioView
from Apps.home.views import HomeView

app_name='home'
urlpatterns = [
    path('', HomeView.as_view(), name='indexapp'),
    path('estudiante/', EstudianteView.as_view(), name='estudianteapp'),
    path('administradores/', AdminView.as_view(), name='administradoresapp'),
    path('acerca_de/', AcercaView.as_view(), name='acercaapp'),
    path('comentarios/', ComentarioView.as_view(), name='acerca1app'),
    path('crear publicacion/', CrearPublicacionView.as_view(),name='publiapp'),
    path('crear comentario/', CrearComentarioView.as_view(),name='comeapp'),
    path('crear articulo/', CrearArticuloView.as_view(),name='artiapp'),
    path('crear autorizacion/', CrearAutorizacionView.as_view(),name='autoapp'),
    path('listado de estudiantes/', ListarEstudianteView.as_view(), name='estudianteapp'),
    path('listado de autorizaciones/', ListarAutorizacionView.as_view(), name='administradoresapp'),
    path('listado de articulos/', ListarArticuloView.as_view(), name='acercaapp'),
    path('listado de comentarios/', ListarComentarioView.as_view(), name='acerca1app'),

]
