from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from check.core.forms import ClienteForm, FornecedorForm, TerceiroForm, BancoForm, EmpresaForm, ChequeForm
from check.core.models import Cliente, Fornecedor, Banco, Terceiro, Empresa, Cheque


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'template.html'


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


class ListTerceiro(LoginRequiredMixin, ListView):
    model = Terceiro
    template_name = 'object_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Terceiro'
        ctx['create_url'] = 'create_terceiro'
        ctx['edit_url'] = 'update_terceiro'
        ctx['delete_url'] = 'delete_terceiro'
        return ctx


class CreateTerceiro(LoginRequiredMixin, CreateView):
    model = Terceiro
    form_class = TerceiroForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_terceiro')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Terceiro'
        return ctx


class UpdateTerceiro(LoginRequiredMixin, UpdateView):
    model = Terceiro
    form_class = TerceiroForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_terceiro')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Terceiro'
        return ctx


class DeleteTerceiro(LoginRequiredMixin, DeleteView):
    model = Terceiro
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_terceiro')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Terceiro'
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


def empresa(request):
    return render(request, "template.html",
                  {"alert_danger": "Você ainda não fez a configuração inicial da sua empresa"})


class UpdateEmpresa(LoginRequiredMixin, UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_empresa')

    def get_object(self):
        print(self.request.user.empresa)
        print(type(self.request.user.empresa))
        e = Empresa.objects.get(id=self.request.user.empresa.id)
        return e;

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Empresa'
        return ctx


class ListCheque(LoginRequiredMixin, ListView):
    model = Cheque
    template_name = 'object_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cheque'
        ctx['create_url'] = 'create_cheque'
        ctx['edit_url'] = 'update_cheque'
        ctx['delete_url'] = 'delete_cheque'
        return ctx


class CreateCheque(LoginRequiredMixin, CreateView):
    model = Cheque
    form_class = ChequeForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cheque')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cheque'
        return ctx


class UpdateCheque(LoginRequiredMixin, UpdateView):
    model = Cheque
    form_class = ChequeForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cheque')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cheque'
        return ctx


class DeleteCheque(LoginRequiredMixin, DeleteView):
    model = Cheque
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_cheque')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cheque'
        return ctx
