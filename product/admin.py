from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields = {'slug':('name',)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
