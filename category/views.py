from django.views.generic import ListView

from product.models import Product
from .models import Category, Subcategory

class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'category/home.html'

class SubcategoryListView(ListView):
    template_name = 'category/subcategory.html'

    def get_queryset(self):
        return Subcategory.objects.filter(category__slug=self.kwargs['slug'])


class ProdDetailListView(ListView):
    template_name = 'product/proddetail.html'

    def get_queryset(self):
        return Product.objects.filter(subcategory__slug__contains=self.kwargs['slug'])
