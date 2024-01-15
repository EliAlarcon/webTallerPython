from django.contrib import admin
from . models import Lodge

# Register your models here.
class LodgeAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Lodge, LodgeAdmin)