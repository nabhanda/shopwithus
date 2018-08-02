from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import SubcategoryListView, ProdDetailListView

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', SubcategoryListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProdDetailListView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)