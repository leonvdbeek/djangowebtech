from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^item/new/$', views.simple_upload, name='simple_upload'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
]
