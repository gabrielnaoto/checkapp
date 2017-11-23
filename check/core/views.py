from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from check.core.forms import ClienteForm, FornecedorForm
from check.core.models import Cliente, Fornecedor


def index(request):
    return render(request, 'template.html', {})


class ListCliente(ListView):
    model = Cliente
    template_name = 'object_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
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
    model = Cliente
    template_name = 'object_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        ctx['edit_url'] = 'update_fornecedor'
        ctx['delete_url'] = 'delete_fornecedor'
        return ctx


class CreateFornecedor(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx


class UpdateFornecedor(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'object_form.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx

class DeleteFornecedor(DeleteView):
    model = Fornecedor
    template_name = 'object_confirm_delete.html'
    success_url = reverse_lazy('list_cliente')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Fornecedor'
        return ctx
