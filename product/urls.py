from django.urls import include, path

from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_changelist'),
    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/', views.ProductUpdateView.as_view(), name='product_change'),
    path('ajax/load-subcategory/', views.load_subcategory, name='ajax_load_subcategory'),
    #path('<int:product_id>', views.detail, name='detail'),

]