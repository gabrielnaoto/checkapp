from django.conf.urls import url, include

from check.core.views import *

urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),

    url(r'^index/', index, name='index'),

    url(r'^cliente/$', ListCliente.as_view(), name='list_cliente'),
    url(r'^cliente/add$', CreateCliente.as_view(), name='create_cliente'),
    url(r'^cliente/edit/(?P<pk>\d+)$', UpdateCliente.as_view(), name='update_cliente'),
    url(r'^cliente/delete/(?P<pk>\d+)$', DeleteCliente.as_view(), name='delete_cliente'),
    
    url(r'^fornecedor/$', ListFornecedor.as_view(), name='list_fornecedor'),
    url(r'^fornecedor/add$', CreateFornecedor.as_view(), name='create_fornecedor'),
    url(r'^fornecedor/edit/(?P<pk>\d+)$', UpdateFornecedor.as_view(), name='update_fornecedor'),
    url(r'^fornecedor/delete/(?P<pk>\d+)$', DeleteFornecedor.as_view(), name='delete_fornecedor'),

    url(r'^banco/$', ListBanco.as_view(), name='list_banco'),
    url(r'^banco/add$', CreateBanco.as_view(), name='create_banco'),
    url(r'^banco/edit/(?P<pk>\d+)$', UpdateBanco.as_view(), name='update_banco'),
    url(r'^banco/delete/(?P<pk>\d+)$', DeleteBanco.as_view(), name='delete_banco'),

    url(r'^terceiro/$', ListTerceiro.as_view(), name='list_terceiro'),
    url(r'^terceiro/add$', CreateTerceiro.as_view(), name='create_terceiro'),
    url(r'^terceiro/edit/(?P<pk>\d+)$', UpdateTerceiro.as_view(), name='update_terceiro'),
    url(r'^terceiro/delete/(?P<pk>\d+)$', DeleteTerceiro.as_view(), name='delete_terceiro'),
]
