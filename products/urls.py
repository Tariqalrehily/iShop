from django.conf.urls import url
from .views import all_products, more_products


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^more_products/$', more_products, name='more_products'),
]
