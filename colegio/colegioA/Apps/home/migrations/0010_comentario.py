# Generated by Django 4.1 on 2022-09-22 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_coment', models.IntegerField()),
                ('creador', models.CharField(max_length=100)),
                ('fecha_com', models.DateField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.publicaciones')),
            ],
        ),
    ]
