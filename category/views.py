from django.views.generic import ListView
from .models import Category, Subcategory

class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = 'category/home.html'

class SubcategoryListView(ListView):
    template_name = 'category/subcategory.html'

    def get_queryset(self):
        return Subcategory.objects.filter(category__slug=self.kwargs['slug'])
