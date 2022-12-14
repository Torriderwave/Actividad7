# Generated by Django 4.1 on 2022-09-22 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_autorizacion_autorizaciones_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacion', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_coment', models.IntegerField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreau', models.CharField(max_length=100)),
                ('tipo1', models.CharField(choices=[('Pub', 'Publico'), ('Priv', 'Privado'), ('Au', 'Autorizado'), ('NoAu', 'No autorizado')], default='Pub', max_length=4)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.publicaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_art', models.IntegerField(verbose_name=30)),
                ('fecha', models.DateField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiante')),
            ],
        ),
    ]
