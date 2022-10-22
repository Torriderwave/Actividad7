
from msilib.schema import ListView
from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from Apps.home.models import Estudiante, Publicaciones, Autorizacion, Articulo,Comentario
from .forms import PublicacionForm,AutorizacionForm,ArticuloForm,ComentarioForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class EstudianteView(TemplateView):
    template_name='Estudiante.html'

class AdminView(TemplateView):
    template_name='Administradores.html'
    
class AcercaView(TemplateView):
    template_name='Acerca de.html'

class ComentarioView(TemplateView):
    template_name='listarcomentarios.html'

class CrearPublicacionView(CreateView):
    template_name='Crear Publicacion.html'
    form_class = PublicacionForm
    success_url=reverse_lazy('home:indexapp')


class CrearComentarioView(CreateView):
    template_name= 'Crear Comentario.html'
    form_class = ComentarioForm
    success_url=reverse_lazy('home:indexapp')


class CrearArticuloView(CreateView):
    template_name= 'Crear Articulo.html'
    form_class = ArticuloForm
    success_url=reverse_lazy('home:indexapp')


class CrearAutorizacionView(CreateView):
    template_name= 'Crear Autorizacion.html'
    form_class = AutorizacionForm
    success_url=reverse_lazy('home:indexapp')

class ListarEstudianteView(ListView):
    template_name='listarestudiante.html'
    model = Publicaciones

    def get_query(self):
        return Estudiante.objects.all()


class ListarAutorizacionView(ListView):
    template_name='listarautorizacion.html'
    model = Autorizacion

    def get_query(self):
        return Estudiante.objects.all()


class ListarArticuloView(ListView):
    template_name='listararticulos.html'
    model = Articulo

    def get_query(self):
        return Estudiante.objects.all()



class ListarComentarioView(ListView):
    template_name='listarcomentarios.html'
    model = Articulo

    def get_query(self):
        return Estudiante.objects.all()

