from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from check.core.forms import ClienteForm, FornecedorForm, TerceiroForm, BancoForm
from check.core.models import Cliente, Fornecedor, Banco, Terceiro


def index(request):
    return render(request, 'template.html', {})


class ListCliente(ListView):
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


class CreateCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
        return ctx


class UpdateCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
        return ctx


class DeleteCliente(DeleteView):
    model = Cliente
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
        return ctx


class ListFornecedor(ListView):
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


class CreateFornecedor(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_fornecedor')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx


class UpdateFornecedor(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_fornecedor')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx


class DeleteFornecedor(DeleteView):
    model = Fornecedor
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_fornecedor')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx


class ListTerceiro(ListView):
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


class CreateTerceiro(CreateView):
    model = Terceiro
    form_class = TerceiroForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_terceiro')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Terceiro'
        return ctx


class UpdateTerceiro(UpdateView):
    model = Terceiro
    form_class = TerceiroForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_terceiro')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Terceiro'
        return ctx


class DeleteTerceiro(DeleteView):
    model = Terceiro
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_terceiro')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Terceiro'
        return ctx


class ListBanco(ListView):
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


class CreateBanco(CreateView):
    model = Banco
    form_class = BancoForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_banco')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Banco'
        return ctx


class UpdateBanco(UpdateView):
    model = Banco
    form_class = BancoForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_banco')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Banco'
        return ctx


class DeleteBanco(DeleteView):
    model = Banco
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_banco')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Banco'
        return ctx
