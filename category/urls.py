from django.conf.urls import url
from .views import SubcategoryListView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', SubcategoryListView.as_view()),
]