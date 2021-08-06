from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models import Count, QuerySet
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from tags.models import TaggedItems
from . import models
# Register your models here.



class InventoryStatus(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [('<10', 'Low')]


    def queryset(self, request, queryset:QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)



class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        "slug":['title']
    }
    search_fields = ['product']
    actions = ['clearInventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_id']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryStatus]
    def collection_id(self, product):
        return product.collection.title


    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    @admin.action(description="Clear Inventory")
    def clearInventory(self, request, queryset):
        update_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f'{update_count} product were successfully updated'
        )



class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']
    search_fields = ['title']


    @admin.display(ordering='product_count')
    def product_count(self, collection):
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
            'collection__id': str(collection.id)
        }))
        return format_html('<a href={}>{}</a>',url, collection.product_count)

    # override the base query set using .get_squryset()
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count = Count('product')
        )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'order_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


    @admin.display(ordering='order_count')
    def order_count(self, customer):
        url_order = (reverse('admin:store_order_changelist')
                    + '?'
                     + urlencode({
                    'customer__id':str(customer.id)
                }))

        return format_html('<a href={}>{}</a>', url_order, customer.order_count)


    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_count = Count('order')
        )



class OrderItemInline(admin.TabularInline):

    min_num = 1
    model = models.OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    list_display = ['id', 'placed_at', 'customer']
    inlines = [OrderItemInline]


admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order, OrderAdmin)