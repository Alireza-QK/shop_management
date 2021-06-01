from django.contrib import admin
from .models import Product, GalleryProduct


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'discount', 'created_at', 'updated_at')


class GalleryProductAdmin(admin.ModelAdmin):
	list_display = ('product', )


admin.site.register(Product, ProductAdmin)
admin.site.register(GalleryProduct, GalleryProductAdmin)
