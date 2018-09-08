from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Category, Subcategory
from product.models import Product


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'category/home.html'


class SubcategoryListView(ListView):
    template_name = 'category/subcategory.html'

    def get_queryset(self):
        return Subcategory.objects.filter(category__slug=self.kwargs['slug'])

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "product/product_list.html"

    def get_queryset(self):
        return Product.objects.filter(subcategory__slug__contains=self.kwargs['slug'])



# class ProdDetailListView(ListView):
#     template_name = 'category/proddetail.html'
#
#     def get_queryset(self):
#         return Product.objects.filter(subcategory__name__icontains=self.kwargs['slug'])

# def product_detail(request, id, slug):
#      product = get_object_or_404(Product, id=id, slug=slug, available=True)
#      return render(request, 'proddetail.html', {'product': product})


