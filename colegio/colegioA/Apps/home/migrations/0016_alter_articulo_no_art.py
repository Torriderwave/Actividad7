# Generated by Django 4.1 on 2022-09-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_articulo_no_art'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='No_art',
            field=models.IntegerField(),
        ),
    ]