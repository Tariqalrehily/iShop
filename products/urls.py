from django.conf.urls import url
from .views import all_products, description


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^description/$', description, name='description')
]
