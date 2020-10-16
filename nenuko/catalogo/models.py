from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Gen(models.Model):
    nomb = models.CharField(max_length=200)

    def __str__(self):
        return self.nomb

class Edito(models.Model):
    nomb = models.CharField(max_length=200)

    def __str__(self):
        return self.nomb

class Manga(models.Model):

    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    resumen = models.TextField(max_length=2000)
    genero = models.ManyToManyField(Gen)
    editorial = models.ManyToManyField(Edito)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apelli = models.CharField(max_length=100)
    naci = models.DateField(null=True, blank=True)
    falle = models.DateField('muerte', null=True, blank=True)

    class Meta:
        ordering = ['apelli', 'nombre']

    def get_absolute_url(self):
        return reverse('detalles-autor', args=[self.id])

    def __str__(self):
        return f'{self.apelli}, {self.nombre}'