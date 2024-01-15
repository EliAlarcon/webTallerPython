from django.db import models

# Create your models here.
class Tour(models.Model):
    title=models.CharField(max_length=200, verbose_name='Título')
    content=models.TextField(verbose_name='Contenido')
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
