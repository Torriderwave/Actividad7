import site
from django.contrib import admin
from .models import  Articulo, Autorizacion, Comentario, Curso, Estudiante, Publicaciones,  Telefono
# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Telefono)
admin.site.register(Publicaciones)
admin.site.register(Autorizacion)
admin.site.register(Articulo)
admin.site.register(Comentario)