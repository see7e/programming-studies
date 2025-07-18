from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomUser, Menu, CustomGroup, CustomSubGroup
from .forms import MultiSelectionGroupForm


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff',)
    search_fields = ('email', 'first_name', 'last_name', 'subgroup__name',)
    list_filter = ('subgroup', 'is_active', 'is_staff',)
    ordering = ('first_name',)
admin.site.register(CustomUser, CustomUserAdmin)


admin.site.unregister(Group) # Unregister the original Group admin.
class GroupAdmin(admin.ModelAdmin):
    form = MultiSelectionGroupForm
    filter_horizontal = ['permissions',] # Filter permissions horizontal as well.
admin.site.register(CustomGroup, GroupAdmin)


class SubGroupAdmin(admin.ModelAdmin):
    model = CustomSubGroup

    list_display = ('name', 'description', 'manager', 'group',)
    search_fields = ('name', 'description', 'manager__first_name', 'manager__last_name', 'group__name',)
    ordering = ('name',)
admin.site.register(CustomSubGroup, SubGroupAdmin)


class MenuAdmin(admin.ModelAdmin):
    model = Menu

    list_display = ('menu', 'submenu', 'url',)
    search_fields = ('menu', 'submenu', 'url',)
    ordering = ('menu',)
admin.site.register(Menu, MenuAdmin)
