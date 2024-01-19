from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Tour(models.Model):
    title=models.CharField(max_length=200, verbose_name='Título')
    content=RichTextField(verbose_name='Contenido')
    image=models.ImageField(upload_to='tours', verbose_name='Imagen')
    url_itineraries=models.URLField(null=True, blank=True, verbose_name="Enlace Itinerario")
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        ordering=['-created']

    def __str__(self):
        return self.title

class Itinerary(models.Model):
    title=models.CharField(max_length=200, verbose_name='Título')
    subtitle=models.CharField(max_length=200, verbose_name='Subtítulo')
    content=RichTextField(verbose_name='Contenido')
    image=models.ImageField(upload_to='tours/itineraries', null=True, blank=True, verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Itinerary'
        verbose_name_plural = 'Itineraries'
        ordering=['-created']

    def __str__(self):
        return self.title