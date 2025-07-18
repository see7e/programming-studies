from django.contrib import admin
from .models import Plugin

class PluginAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'author', 'category', 'create_date', 'update_date')
    search_fields = ('name', 'author', 'category')
    list_filter = ('category', 'author', 'create_date', 'update_date')

admin.site.register(Plugin, PluginAdmin)