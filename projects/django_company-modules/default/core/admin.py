from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("description", "application", "timestamp")
    search_fields = ("description", "application", "timestamp")
    list_filter = ("description", "application", "timestamp")
    ordering = ("timestamp",)


admin.site.register(Event, EventAdmin)
