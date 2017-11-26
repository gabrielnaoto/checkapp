from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.db.models import Sum
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from check.core.forms import ClienteForm, FornecedorForm, BancoForm, EmpresaForm, ChequeEmitidoForm, ChequeRecebidoForm
from check.core.models import Cliente, Fornecedor, Banco, Empresa, Emitido, Recebido


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        total_emitido = Emitido.objects.all().aggregate(Sum('valor'))
        if total_emitido['valor__sum'] is not None:
            ctx['total_emitido'] = total_emitido
        total_recebido = Recebido.objects.all().aggregate(Sum('valor'))
        if total_recebido['valor__sum'] is not None:
            ctx['total_recebido'] = total_recebido
        return ctx


class ListCliente(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'object_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
        ctx['create_url'] = 'create_cliente'
        ctx['edit_url'] = 'update_cliente'
        ctx['delete_url'] = 'delete_cliente'
        return ctx


class CreateCliente(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
        return ctx


class UpdateCliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
        return ctx


class DeleteCliente(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
        return ctx


class ListFornecedor(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = 'object_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        ctx['create_url'] = 'create_fornecedor'
        ctx['edit_url'] = 'update_fornecedor'
        ctx['delete_url'] = 'delete_fornecedor'
        return ctx


class CreateFornecedor(LoginRequiredMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_fornecedor')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx


class UpdateFornecedor(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_fornecedor')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx


class DeleteFornecedor(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_fornecedor')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx


class ListBanco(LoginRequiredMixin, ListView):
    model = Banco
    template_name = 'object_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Banco'
        ctx['create_url'] = 'create_banco'
        ctx['edit_url'] = 'update_banco'
        ctx['delete_url'] = 'delete_banco'
        return ctx


class CreateBanco(LoginRequiredMixin, CreateView):
    model = Banco
    form_class = BancoForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_banco')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Banco'
        return ctx


class UpdateBanco(LoginRequiredMixin, UpdateView):
    model = Banco
    form_class = BancoForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_banco')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Banco'
        return ctx


class DeleteBanco(LoginRequiredMixin, DeleteView):
    model = Banco
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_banco')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Banco'
        return ctx


class UpdateEmpresa(LoginRequiredMixin, UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        print(self.request.user.empresa)
        print(type(self.request.user.empresa))
        try:
            return Empresa.objects.get(id=self.request.user.empresa.id)
        except Exception:
            return None;

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Empresa'
        if self.get_object() == None:
            ctx['alert_danger'] = 'Você ainda não fez a configuração inicial da sua empresa'
        return ctx


class ListChequeEmitido(LoginRequiredMixin, ListView):
    model = Emitido
    template_name = 'cheque_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Emissão'
        ctx['create_url'] = 'create_cheque_emissao'
        ctx['edit_url'] = 'update_cheque_emissao'
        ctx['delete_url'] = 'delete_cheque_emissao'
        return ctx


class CreateChequeEmitido(LoginRequiredMixin, CreateView):
    model = Emitido
    form_class = ChequeEmitidoForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cheque_emissao')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Emissão'
        return ctx


class UpdateChequeEmitido(LoginRequiredMixin, UpdateView):
    model = Emitido
    form_class = ChequeEmitidoForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cheque_emissao')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Emissão'
        return ctx


class DeleteChequeEmitido(LoginRequiredMixin, DeleteView):
    model = Emitido
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_cheque_emissao')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Recebimento'
        return ctx


class ListChequeRecebido(LoginRequiredMixin, ListView):
    model = Recebido
    template_name = 'cheque_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Recebimento'
        ctx['create_url'] = 'create_cheque_recebimento'
        ctx['edit_url'] = 'update_cheque_recebimento'
        ctx['delete_url'] = 'delete_cheque_recebimento'
        return ctx


class CreateChequeRecebido(LoginRequiredMixin, CreateView):
    model = Recebido
    form_class = ChequeRecebidoForm
    template_name = 'cheque_recebimento_form.html'
    success_url = reverse_lazy('list_cheque_recebimento')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Recebimento'
        return ctx


class UpdateChequeRecebido(LoginRequiredMixin, UpdateView):
    model = Recebido
    form_class = ChequeRecebidoForm
    template_name = 'cheque_recebimento_form.html'
    success_url = reverse_lazy('list_cheque_recebimento')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Recebimento'
        return ctx


class DeleteChequeRecebido(LoginRequiredMixin, DeleteView):
    model = Recebido
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_cheque_recebimento')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Recebimento'
        return ctx


class BaixaChequesView(ListView):
    template_name = 'baixa.html'
    model = Recebido

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Controle de cheques'
        ctx['bread_item'] = 'Baixa de cheques'
        return ctx


def get_situacao_cliente(request):
    id = request.GET.get('id')
    recebidos = len(list(Recebido.objects.filter(cliente_id=id).filter(tem_fundo=False)))
    ctx = {'quantidade': recebidos}
    return JsonResponse(ctx)


def efetuar_baixa(request):
    id = request.GET.get('id')
    tem_fundo = request.GET.get('tem_fundo')
    if tem_fundo == 'true':
        tem_fundo = True
    else:
        tem_fundo = False
    print(id)
    print(tem_fundo)
    cheque = Recebido.objects.get(id=id)
    cheque.tem_fundo = tem_fundo
    cheque.foi_compensado = True
    cheque.save()
    ctx = {'status': True}
    return JsonResponse(ctx)
