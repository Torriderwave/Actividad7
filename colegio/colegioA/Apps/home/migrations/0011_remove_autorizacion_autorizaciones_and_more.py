# Generated by Django 4.1 on 2022-09-22 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autorizacion',
            name='autorizaciones',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='publicaciones',
            name='publicaciones',
        ),
        migrations.DeleteModel(
            name='Articulo',
        ),
        migrations.DeleteModel(
            name='Autorizacion',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Publicaciones',
        ),
    ]