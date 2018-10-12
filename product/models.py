from django.contrib.sessions import serializers
from django.db import models
from django.db.models import CASCADE, Q
from django.urls import reverse
from django.utils.functional import empty

from category.models import Subcategory, Category
from category.utils import unique_slugify

class ProductQuerySet(models.query.QuerySet):
    def available(self):
        return self.filter(available=True)

    def search(self, query):
        lookups = (Q(name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query)
                   # Q(category__icontains=query) |
                   # Q(subcategory__icontains=query)
                   )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()
#
# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model, using=self._db)
#
#     def all(self):
#         return self.get_queryset().available()
#
#     def get_by_id(self, id):
#         qs = self.get_queryset().filter(id=id)
#         if qs.count() == 1:
#             return qs.first()
#         return None


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().available()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().available().search(query)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    stock = models.PositiveIntegerField(blank=False,default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        get_latest_by = 'created'

    def get_absolute_url(self):
        return "/product/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        slug_str = "%s %s %s" % (self.name, self.category, self.subcategory)
        unique_slugify(self, slug_str)
        super(Product, self).save(**kwargs)


    # def get_absolute_url(self):
    #     return reverse('product:detail', args=[self.id, self.slug])

# class AddProductToCartSerializer(AddToCartSerializer):
#     stock = serializers.PositiveIntegerField(read_only=True)
#
#     def get_instance(self, context, data, extra_args):
#         product = context['product']
#         product.refresh_from_db()
#         if data != empty:
#             quantity = data.get('quantity', self.fields['quantity'].default)
#             data['quantity'] = min(int(quantity), product.amount_in_stock)
#         instance = super().get_instance(context, data, extra_args)
#         instance.update(
#             stock=product.stock,
#         )
#         return instance