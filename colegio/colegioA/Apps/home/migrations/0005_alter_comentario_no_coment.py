# Generated by Django 4.1 on 2022-09-17 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_publicaciones_comentario_autorizacion_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='No_coment',
            field=models.IntegerField(),
        ),
    ]
