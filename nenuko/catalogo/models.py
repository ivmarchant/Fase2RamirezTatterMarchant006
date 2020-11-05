from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Manga(models.Model):
    
	titulo = models.CharField(max_length=200)
	Mangaka = models.ForeignKey('Mangaka', on_delete=models.SET_NULL, null=True)
    
	summary = models.TextField(max_length=1000)
	volumen = models.CharField('Volumen', max_length=13)
	genre = models.ManyToManyField(Genre)
    
	def __str__(self):
		return self.titulo
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this manga."""
		return reverse('manga-detail', args=[str(self.id)])

class MangaInstance(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    manga= models.ForeignKey('Manga', on_delete=models.SET_NULL, null=True)
    fecha= models.DateField(null=True, blank=True)

    STOCK_STATUS= (
        ('s', 'Stock Disponible'),
        ('n', 'Stock no Disponible'),
    )
    status = models.CharField(
        max_length=2,
        choices=STOCK_STATUS,
        blank=True,
        default='s',
    )
    class Meta:
        ordering = ['fecha']
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.manga.titulo})'
class Mangaka(models.Model):
	"""Model representing an Mangaka."""
	primer_nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField(null=True, blank=True)
	fecha_muerte = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['apellido', 'primer_nombre']

	def get_absolute_url(self):
		return reverse('mangaka-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.apellido}, {self.primer_nombre}'	
