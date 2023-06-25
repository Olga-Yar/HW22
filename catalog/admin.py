from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'date_create', 'is_public', 'image')
    search_fields = ('title', 'date_create', 'is_public')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_name', 'is_active')
    search_fields = ('product', 'version_number', 'version_name', 'is_active')
