from django.conf.urls import url
from .views import products, more_products, product_view


urlpatterns = [
    url(r'^$', products, name='products'),
    url(r'^more_products/$', more_products, name='more_products'),
    url(r'^(?P<slug>[\w-]+)$', product_view, name='product_view'),
]
