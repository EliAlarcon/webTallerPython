from django.contrib import admin
from . models import Lodge, Section, DetailSection

# Register your models here.
class LodgeAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Lodge, LodgeAdmin)

class SectionAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Section, SectionAdmin)

class DetailSectionAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(DetailSection, DetailSectionAdmin)