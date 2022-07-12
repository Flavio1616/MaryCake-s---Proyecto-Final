from django.contrib import admin
from .models import Torta

# Register your models here.
class TortaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Torta, TortaAdmin)
