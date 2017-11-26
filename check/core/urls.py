from django.conf.urls import url, include

from check.core.views import *

urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),

    url(r'^index/', IndexView.as_view(), name='index'),

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

    url(r'^empresa/$', UpdateEmpresa.as_view(), name='empresa'),

    url(r'^cheque/emitir/$', ListChequeEmitido.as_view(), name='list_cheque_emissao'),
    url(r'^cheque/emitir/add$', CreateChequeEmitido.as_view(), name='create_cheque_emissao'),
    url(r'^cheque/emitir/edit/(?P<pk>\d+)$', UpdateChequeEmitido.as_view(), name='update_cheque_emissao'),
    url(r'^cheque/emitir/delete/(?P<pk>\d+)$', DeleteChequeEmitido.as_view(), name='delete_cheque_emissao'),

    url(r'^cheque/receber/$', ListChequeRecebido.as_view(), name='list_cheque_recebimento'),
    url(r'^cheque/receber/add$', CreateChequeRecebido.as_view(), name='create_cheque_recebimento'),
    url(r'^cheque/receber/edit/(?P<pk>\d+)$', UpdateChequeRecebido.as_view(), name='update_cheque_recebimento'),
    url(r'^cheque/receber/delete/(?P<pk>\d+)$', DeleteChequeRecebido.as_view(), name='delete_cheque_recebimento'),

    url(r'^baixa/$', BaixaChequesView.as_view(), name='baixa'),
    url(r'^repasse/$', RepasseChequesView.as_view(), name='repasse'),

    url(r'^ajax/get_situacao_cliente/$', get_situacao_cliente, name='get_situacao_cliente'),
    url(r'^ajax/efetuar_baixa/$', efetuar_baixa, name='efetuar_baixa'),
    url(r'^ajax/efetuar_repasse/$', efetuar_repasse, name='efetuar_repasse'),
]
