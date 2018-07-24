from django.contrib import admin
from .models import Category, Subcategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields = {'slug':('name',)}
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)



class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    prepopulated_fields = {'slug':('name',)}
    class Meta:
        model = Subcategory

admin.site.register(Subcategory, SubcategoryAdmin)