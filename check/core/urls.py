from django.conf.urls import url, include

from check.core.views import index, ListCliente, UpdateCliente, CreateCliente

urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),

    url(r'^index/', index, name='index'),

    url(r'^cliente/', ListCliente.as_view(), name='list_cliente'),
    url(r'^cliente/add/', CreateCliente.as_view(), name='create_cliente'),
    url(r'^cliente/edit/(?P<pk>\d+)$', UpdateCliente.as_view(), name='update_cliente'),
]
