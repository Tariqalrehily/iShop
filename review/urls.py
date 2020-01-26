from django.conf.urls import url
from .views import reviews_list, add_review


urlpatterns = [
    url(r'^$', reviews_list, name='reviews_list'),
    url(r'^add_review/$', add_review, name='add_review'),
]
