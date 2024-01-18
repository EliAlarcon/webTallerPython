from django.db import models

# Create your models here.
class Lodge(models.Model):
    title=models.CharField(max_length=200, verbose_name='Título')
    nombre=models.CharField(max_length=200, verbose_name='Nombre Lodge')
    subtema=models.CharField(max_length=200, verbose_name='Subtema')
    content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(upload_to='tours', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Lodge'
        verbose_name_plural = 'Lodges'
        ordering=['-created']

    def __str__(self):
        return self.title
    

# Modelos con relaciones a Lodge
""" class Contenido(models.Model):
    name=models.CharField(max_length=100, verbose_name='Título del contenido')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

    def __str__(self):
        return  """