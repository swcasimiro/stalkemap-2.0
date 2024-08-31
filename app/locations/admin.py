from django.contrib import admin

from django.utils.safestring import mark_safe

from .models import Location, Hood


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Hood)
class HoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
