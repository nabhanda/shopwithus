from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category','subcategory', 'description', 'image', 'price', 'stock', 'available', 'created']
    # search_fields = ['traduttore__nome", "linguaDa__field1", "linguaA_field2"]
    list_filter = ['category','subcategory', 'available', 'created']
    list_editable = ['category','subcategory', 'price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
