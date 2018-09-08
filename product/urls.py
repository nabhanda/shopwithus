from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from product.views import product_detail_view, ProductListView, ProductDetailView, ProductCreateView
# ProductDetailView
from . import views

urlpatterns = [
    path('add/', ProductCreateView.as_view(), name='product_add'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view()),
    #url(r'^$', ProductListView.as_view()),
    #url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view()),
    path('<int:pk>/', views.ProductUpdateView.as_view(), name='product_change'),
    path('ajax/load-subcategory/', views.load_subcategory, name='ajax_load_subcategory'),
    #path('<int:id>/', views.product_detail_view, name='product_changelist'),
    ##########################ProductAddPage#########################
    # url(r'^$', views.product_list, name='product_list'),
    #path('<subcategory_slug>/', ProductDetailView.as_view(), name='product_detail'),
    #url(r'^(?P<subcategory_slug>[\w-]+)/$', ProductDetailView, name='product_detail'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)