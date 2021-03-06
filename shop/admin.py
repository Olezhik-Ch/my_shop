from django.contrib import admin
from shop.models import *


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'category', 'price', 'stock', 'available',]
	list_filter = ['available', 'category',]
	search_fields = ['product_name', 'category',]
	prepopulated_fields = {'slug': ('product_name',)}


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name', 'slug']
	prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
