from django.contrib import admin
from .models import Tour

# Register your models here.
class TourAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Tour, TourAdmin)