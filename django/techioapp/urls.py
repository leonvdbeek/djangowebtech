from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^howdoesitwork/$', views.howdoesitwork, name='howdoesitwork'),
    url(r'^shoppingcart/$', views.shoppingcart, name='shoppingcart'),
    url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^item/(?P<pk>\d+)/remove/$', views.item_remove, name='item_remove'),
    url(r'^items/$', views.ItemList.as_view()),
    url(r'^items/(?P<pk>[0-9]+)$', views.ItemListElement.as_view()),
    url(r'^parties/$', views.PartyList.as_view()),
    url(r'^parties/(?P<pk>[0-9]+)$', views.PartyListElement.as_view()),
    url(r'^organized/(?P<pk>[0-9]+)$', views.organizedView.as_view()),
    url(r'^saved/(?P<pk>[0-9]+)$', views.savedView.as_view()),
    url(r'^todayParty/$', views.todayView.as_view()),
    url(r'^futureParty/$', views.futureView.as_view()),
    url(r'^save/$', views.saveView.as_view()),
    url(r'^userid/$', views.useridView.as_view()),
    url(r'^userids/$', views.alluseridView.as_view()),
    url(r'^unsave/(?P<userid>[0-9]+)/(?P<partyid>[0-9]+)$', views.unsaveView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
