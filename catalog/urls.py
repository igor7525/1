from django.conf.urls import url
from catalog import views

urlpatterns = [
    url(r'^(?P<category>[a-z0-9-]+)/$', views.catalog_list, name='catlog-list'),
    url(r'^(?P<category>[a-z0-9-]+)/ajax/$', views.ajax, name='ajax-filter-products'),
    url(r'^(?P<category>[a-z0-9-]+)/position-(?P<id>[0-9]+)/$', views.detail, name='catlog-detail')
]
