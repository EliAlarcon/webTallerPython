from django.db import models

# Create your models here.
class Lodge(models.Model):
    title=models.CharField(max_length=200, verbose_name='Título')
    nombre=models.CharField(max_length=200, verbose_name='Nombre Lodge')
    subtema=models.CharField(max_length=200, verbose_name='Subtema')
    content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(upload_to='tours', verbose_name='Imagen')
    sections=models.ManyToManyField('Section', verbose_name='Secciones')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Lodge'
        verbose_name_plural = 'Lodges'
        ordering=['-created']

    def __str__(self):
        return self.title
    

# Modelos con relaciones a Lodge
class Section(models.Model):
    name=models.CharField(max_length=100, verbose_name='Nombre de la Sección')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
        ordering=['name']

    def __str__(self):
        return self.name
    
class DetailSection(models.Model):
    name=models.CharField(max_length=100, verbose_name='Título')
    content=models.TextField(verbose_name='Detalle Sección')
    image=models.ImageField(upload_to='lodges', verbose_name='Imagen')
    lodge=models.ForeignKey(Lodge, on_delete=models.CASCADE, verbose_name='Lodge')
    section=models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Sección')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Detail Content'
        verbose_name_plural = 'Detail Content'
        ordering=['-created']

    def __str__(self):
        return self.name