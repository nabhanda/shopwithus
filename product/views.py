from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from category.models import Subcategory
from product.forms import ProductForm
from product.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    #fields = ('category', 'subcategory', 'name', 'description', 'image', 'price', 'stock', 'available')
    success_url = reverse_lazy('home')

class PersonUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    #fields = ('category', 'subcategory', 'name', 'description', 'image', 'price', 'stock', 'available')
    success_url = reverse_lazy('home')

def load_subcategory(request):
    category_id = request.GET.get('category')
    subcategory = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'product/subcategory_dropdown_list_options.html', {'subcategory': subcategory})
