# Generated by Django 5.0.1 on 2024-01-19 07:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_itinerary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
