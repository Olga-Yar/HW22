from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_lot', 'image')
    search_fields = ('name', 'about',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about')
    # list_filter = ('category',)
    search_fields = ('name', 'about',)
