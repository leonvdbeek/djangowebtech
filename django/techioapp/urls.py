from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^howdoesitwork$', views.todo_new, name='howdoesitwork'),
    url(r'^shoppingcart$', views.todo_new, name='shoppingcart'),
    url(r'^index$', views.todo_new, name='index'),
]
