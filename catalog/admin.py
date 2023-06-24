from django.contrib import admin

from catalog.models import Product, Category, Blog


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
