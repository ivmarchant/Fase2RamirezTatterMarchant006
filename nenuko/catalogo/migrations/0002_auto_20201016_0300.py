# Generated by Django 3.1.2 on 2020-10-16 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['apelli', 'nombre']},
        ),
    ]
