from django.db import models
from django.db.models import CASCADE
from django.urls import reverse

from category.models import Subcategory, Category

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=CASCADE)
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category:product_details', args=[self.id, self.slug])
