from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from category.models import Subcategory
from product.forms import ProductForm
from product.models import Product



class ProductListView(ListView):
    model = Product
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_changelist')

def productlist(request, product_id):
    product = Product.objects.get(productid=product_id)
    return render(request, 'product/product_list.html', {'product': product})

# def productlist(request):
#     prodlist = Product.objects.order_by('-pk')[0]
#     return render(request, 'product/product_list.html', {'prodlist': prodlist})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_changelist')

def load_subcategory(request):
    category_id = request.GET.get('category')
    subcategory = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'product/subcategory_dropdown_list_options.html', {'subcategory': subcategory})




