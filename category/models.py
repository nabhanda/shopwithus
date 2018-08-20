from django.db import models
from django.db.models import CASCADE
from django.urls import reverse

from .utils import unique_slugify

class Category(models.Model):
     image = models.ImageField(upload_to='images/', blank=True)
     name = models.CharField(max_length=200, db_index=True)
     slug = models.SlugField(max_length=200, db_index=True, blank=True)

     class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

     def get_absolute_url(self):
         return '/category/{slug}/'.format(slug=self.slug)

     def __str__(self):
         return self.name

     def save(self, **kwargs):
         slug_str = "%s" % (self.name)
         unique_slugify(self, slug_str)
         super(Category, self).save(**kwargs)

class Subcategory(models.Model):
     category = models.ForeignKey(Category, on_delete=CASCADE)
     image = models.ImageField(upload_to='images/', blank=True)
     name = models.CharField(max_length=200, db_index=True)
     slug = models.SlugField(max_length=200, db_index=True, blank=True)

     class Meta:
         ordering = ('name',)
         verbose_name = 'subcategory'
         verbose_name_plural = 'subcategories'

     def __str__(self):
         return self.name

     def save(self, **kwargs):
         slug_str = "%s %s" % (self.name, self.category)
         unique_slugify(self, slug_str)
         super(Subcategory, self).save(**kwargs)
