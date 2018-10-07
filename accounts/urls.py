from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import LoginView, RegisterView, guest_register_view

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/guest/$', guest_register_view, name='guest_register'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)