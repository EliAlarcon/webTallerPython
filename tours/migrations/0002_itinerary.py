# Generated by Django 5.0.1 on 2024-01-19 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tours/itineraries', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Itinerary',
                'verbose_name_plural': 'Itineraries',
                'ordering': ['-created'],
            },
        ),
    ]
