from django.http import Http404, request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from category.models import Subcategory
from product.forms import ProductForm
from product.models import Product
from carts.models import Cart


##############THis is for the Product Add page#################
# class ProductListView(ListView):
#     model = Product
#     context_object_name = 'product'
#     queryset = Product.objects.filter()


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "product/product_list.html"

    def get_queryset(self):
        return Product.objects.filter(subcategory__slug__contains=self.kwargs['slug'])

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/product_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        print(context)
        return context

# class ProductDetailView(DetailView):
#     model = Product
#     context_object_name = 'product'
#     template_name = "product_list.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
#         return context

##########################################################################################################
# class ProductDetailView(DetailView):
#     model = Product
#     #queryset = Product.objects.all()
#     template_name = "product_detail.html"
#
#     # def get_object(self, queryset=None):
#     #     request = self.request
#     #     subcategory_slug = self.kwargs.get('slug')
#     #     instance = get_object_or_404(Product, slug__icontains=subcategory_slug)
#     #     if instance is None:
#     #         raise Http404("Product Does not exist")
#     #     return instance
#
#     def get_object(self, *args, **kwargs):
#         request = self.request
#         pk=self.kwargs.get('pk')
#         instance = Product.objects.get_by_id(pk)
#         if instance is None:
#             raise Http404("Product Does not exists")
#         return instance
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
#         return context
################################################################################################################3
# class ProductDetailView(DetailView):
#     template_name = 'product/product_list.html'
#     #model = User
#     #context_object_name = 'foo'
#
#     def get_object(self):
#         #return get_object_or_404(Product, pk=request.session['product_id'])
#         return get_object_or_404(Product, pk=self.request.

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product_form.html"
    success_url = reverse_lazy('home')

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

####################Code for Product Add page ends here#####################################

# def product_list(request, subcategory_slug=None):
#     subcategory = None
#     subcategories = Subcategory.objects.all()
#     products = Product.objects.filter(available=True)
#     if subcategory_slug:
#         subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
#         products = products.filter(subcategory=subcategory)
#     return render(request, 'prodlist.html', {'subcategory':subcategory, 'subcategories':subcategories, 'products':products})
#
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     #cart_product_form = CartAddProductForm()
#     return render(request, 'proddetail.html', {'product':product})

def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    print(instance)
    qs = Product.objects.filter(id=pk)
    print(qs)
    p = qs.count()
    print(p)

    if qs.exists() or qs.count() > 1:
        instance = qs.first()
    else:
        raise Http404("Product NOOT found")

    context = {
        'object':instance
    }
    return render(request, "product/product_detail.html", context)
