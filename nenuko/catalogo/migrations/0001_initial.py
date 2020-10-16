# Generated by Django 3.1.2 on 2020-10-16 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apelli', models.CharField(max_length=100)),
                ('naci', models.DateField(blank=True, null=True)),
                ('falle', models.DateField(blank=True, null=True, verbose_name='muerte')),
            ],
        ),
        migrations.CreateModel(
            name='Edito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomb', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomb', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('resumen', models.TextField(max_length=2000)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.autor')),
                ('editorial', models.ManyToManyField(to='catalogo.Edito')),
                ('genero', models.ManyToManyField(to='catalogo.Gen')),
            ],
        ),
    ]