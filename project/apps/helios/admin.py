from django.contrib import admin
from .models import HTTPRequest

# Register your models here.
class HTTPRequestAdmin(admin.ModelAdmin):
    list_display = ('method', 'url', 'duration',)

admin.site.register(HTTPRequest, HTTPRequestAdmin)