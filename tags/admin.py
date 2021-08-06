from django.contrib import admin
from .models import Tags


class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']

admin.site.register(Tags, TagAdmin)