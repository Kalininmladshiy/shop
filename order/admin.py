from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created',
                    'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['get_image_preview']

    def get_image_preview(self, product):
        return format_html('<img src="/media/{}" height=200px width=auto />', product.image)
    get_image_preview.short_description = 'превью'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'phonenumber', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated', 'phonenumber', 'address']
    inlines = [OrderItemInline]
