from django.conf.urls import url
from .views import do_search, filter

urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^filter/', filter, name='filter')
]