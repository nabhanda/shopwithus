from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import login_page, register_page

urlpatterns = [
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)