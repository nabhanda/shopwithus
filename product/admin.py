from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','subcategory', 'description', 'image', 'price', 'stock', 'available', 'created']
    list_filter = ['category','subcategory', 'price', 'available', 'created']
    list_editable = ['category','subcategory', 'price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
