from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Publicaciones, Comentario, Articulo, Autorizacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model=Publicaciones
        fields='__all__'


class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields='__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model=Articulo
        fields='__all__'

class AutorizacionForm(forms.ModelForm):
    class Meta:
        model=Autorizacion
        fields='__all__'

