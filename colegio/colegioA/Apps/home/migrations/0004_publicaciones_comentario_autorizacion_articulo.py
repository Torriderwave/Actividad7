# Generated by Django 4.1 on 2022-09-17 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacion1', models.CharField(max_length=100)),
                ('creador', models.CharField(max_length=100)),
                ('autorizacion', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('Estudiante', models.ManyToManyField(to='home.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_coment', models.IntegerField(verbose_name=30)),
                ('creador', models.CharField(max_length=100)),
                ('fecha_com', models.DateField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('Estudiante', models.ManyToManyField(to='home.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacion', models.CharField(max_length=100)),
                ('autorizacion', models.CharField(max_length=100)),
                ('tipo1', models.CharField(choices=[('Pub', 'Publico'), ('Priv', 'Privado'), ('Au', 'Autorizado'), ('NoAu', 'No autorizado')], default='Pub', max_length=4)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_art', models.IntegerField(verbose_name=30)),
                ('creador', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('Estudiante', models.ManyToManyField(to='home.estudiante')),
            ],
        ),
    ]