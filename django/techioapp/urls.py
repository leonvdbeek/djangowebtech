from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^howdoesitwork/$', views.howdoesitwork, name='howdoesitwork'),
    url(r'^shoppingcart/$', views.shoppingcart, name='shoppingcart'),
    url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^item/(?P<pk>\d+)/remove/$', views.item_remove, name='item_remove'),
]
