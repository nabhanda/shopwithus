from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path

from category import views
from .views import SubcategoryListView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', SubcategoryListView.as_view()),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    #url(r'^(?P<slug>[\w-]+)/$', ProdDetailListView.as_view()),
    #path('prodlistdetail/', views.ProdDetailListView.as_view(), name='product_list_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)