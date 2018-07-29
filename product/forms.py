from django import forms

from category.models import Subcategory
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'name', 'description', 'image', 'price', 'stock', 'available')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Subcategory queryset
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('name')