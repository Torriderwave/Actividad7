from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class EstudianteView(TemplateView):
    template_name='Estudiante.html'

class AdminView(TemplateView):
    template_name='Administradores.html'
    
class AcercaView(TemplateView):
    template_name='Acerca de.html'