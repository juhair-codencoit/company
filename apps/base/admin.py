from django.contrib import admin
from .models import *

@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {"slug":("name",)}
    ordering = ['name']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'page_name']
    ordering = ['name', 'page_name']