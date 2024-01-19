from django.contrib import admin
from .models import Tour, Itinerary

# Register your models here.
class TourAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Tour, TourAdmin)

class IntineraryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Itinerary, IntineraryAdmin)