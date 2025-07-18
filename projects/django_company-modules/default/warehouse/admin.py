from django.contrib import admin
from core.models import Event, Task
from .models import Event, OutboundRequest, Item, Rack, Shed


class OutboundRequestAdmin(admin.ModelAdmin):
    list_display = ("license_plate", "task", "destination_code")
    search_fields = ("license_plate", "task", "destination_code")
    list_filter = ("license_plate", "task", "destination_code")
    ordering = ("task",)


admin.site.register(OutboundRequest, OutboundRequestAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "type",
        "status",
        "start_date",
        "due_date",
    )
    search_fields = ("name", "description", "user", "type", "status")
    list_filter = (
        "name",
        "description",
        "type",
        "status",
        "start_date",
        "due_date",
    )
    ordering = ("start_date",)


admin.site.register(Task, TaskAdmin)


# class ReportAdmin(admin.ModelAdmin):
#     list_display = ('user', 'manager', 'description', 'date')
#     search_fields = ('user', 'manager', 'description', 'date')
#     list_filter = ('user', 'manager', 'description', 'date')
#     ordering = ('date',)
# admin.site.register(Report, ReportAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "description", "quantity", "in_rack")
    search_fields = ("code", "name", "description")
    list_filter = ("in_rack", "name", "description", "quantity")
    ordering = ("in_rack",)


admin.site.register(Item, ItemAdmin)


class RackAdmin(admin.ModelAdmin):
    list_display = ("code", "capacity", "in_shed")
    search_fields = ("code", "capacity", "in_shed")
    list_filter = ("code", "capacity", "in_shed")
    ordering = ("code",)


admin.site.register(Rack, RackAdmin)


class ShedAdmin(admin.ModelAdmin):
    list_display = ("shed", "capacity")
    search_fields = ("shed", "capacity")
    list_filter = ("shed", "capacity")
    ordering = ("shed",)


admin.site.register(Shed, ShedAdmin)
