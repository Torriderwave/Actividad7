#from lzma import _FilterChain
from doctest import master
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=200)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s' % (self.nombre)

class Telefono(models.Model):
    tipo_telefono=(
        ('C','Casa'),
        ('M','Celular'),
        ('T','Trabajo'),
    )
    Telefono = models.CharField(max_length=13)
    Estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    tipo = models.CharField(
        max_length=1,
        choices=tipo_telefono,
        default='C',
    )
    creacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s' % (self.Telefono)

class Publicaciones(models.Model):
    publicacion1 = models.CharField(max_length=100)
    creador = models.CharField(max_length=100)
    autorizacion=models.CharField(max_length=100)
    creacion = models.DateTimeField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s %s %s' % (self.publicacion1,self.creador,self.autorizacion)

class Autorizacion(models.Model):
    publicacion = models.CharField(max_length=100)
    autorizacion=models.CharField(max_length=100)
    tipo_au=(
        ('Pub','Publico'),
        ('Priv','Privado'),
        ('Au','Autorizado'),
        ('NoAu','No autorizado'),

    )
    
    Estudiante = models.ForeignKey(Estudiante,on_delete=models.CASCADE)
    tipo1 = models.CharField(
        max_length=4,
        choices=tipo_au,
        default='Pub',
    )
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.publicacion,self.autorizacion)

    
class Articulo(models.Model):
    No_art = models.IntegerField(30)
    creador = models.CharField(max_length=100)
    fecha = models.DateField()
    creacion = models.DateTimeField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s' % (self.No_art,self.creador,self.fecha)


class Comentario(models.Model):
    No_coment = models.IntegerField()
    creador = models.CharField(max_length=100)
    fecha_com = models.DateField()
    creacion = models.DateTimeField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s' % (self.No_coment,self.creador,self.fecha_com)



