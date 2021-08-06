from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.models import Product
from tags.models import TaggedItems

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tags']
    model = TaggedItems

class CustomProductAdmin(admin.ModelAdmin):
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)


