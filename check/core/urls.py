from django.conf.urls import url, include

from check.core.views import index, ListCliente, UpdateCliente, CreateCliente, DeleteCliente, DeleteFornecedor, \
    UpdateFornecedor, CreateFornecedor, ListFornecedor

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
]
