# Generated by Django 4.1 on 2022-09-22 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_creador_articulo_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='creador',
            new_name='nombre',
        ),
    ]
