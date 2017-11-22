from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView

from check.core.forms import ClienteForm
from check.core.models import Cliente


def index(request):
    return render(request, 'template.html', {})


class ListCliente(ListView):
    model = Cliente
    template_name = 'object_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['bread_menu'] = 'Cadastros'
        ctx['bread_item'] = 'Cliente'
        return ctx


class CreateCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'object_form.html'

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx['bread_menu'] = 'Cadastros'
    #     ctx['bread_item'] = 'Cliente'
    #     return ctx


class UpdateCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'object_form.html'

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx['bread_menu'] = 'Cadastros'
    #     ctx['bread_item'] = 'Cliente'
    #     return ctx
