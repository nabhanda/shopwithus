from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from carts import views
from .views import cart_home, cart_update, checkout_home, chechout_done_view

urlpatterns = [
    url(r'^$', cart_home, name='cart'),
    url(r'^checkout/success/$', chechout_done_view, name='success'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
    # path('', cart_home, name='home'),
    # path('update/', cart_update, name='update'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)