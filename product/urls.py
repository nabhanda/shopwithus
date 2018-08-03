from django.conf.urls import url
from django.urls import include, path

from product.views import ProductDetailView
from . import views


urlpatterns = [
    path('', views.ProductDetailView.as_view(), name='product_changelist'),
    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/', views.ProductUpdateView.as_view(), name='product_change'),
    path('ajax/load-subcategory/', views.load_subcategory, name='ajax_load_subcategory'),
    ##########################ProductAddPage#########################
    # url(r'^$', views.product_list, name='product_list'),
    # url(r'^(?P<subcategory_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]