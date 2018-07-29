from django.urls import include, path

from . import views


urlpatterns = [
    path('add/', views.ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='product_change'),
    path('ajax/load-subcategory/', views.load_subcategory, name='ajax_load_subcategory'),

]