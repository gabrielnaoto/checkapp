from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    url(r'^cliente/$', views.ClienteList.as_view(), name='cliente_list'),
    url(r'^cliente/new$', views.ClienteCreate.as_view(), name='cliente_new'),
    url(r'^cliente/edit/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name='cliente_edit'),
    url(r'^cliente/delete/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name='cliente_delete'),
]
