from django.shortcuts import render
from .models import Cliente
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,ListView, View
from .forms import *
# Create your views here.

class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')
    form_class = ClienteForm

class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')
    form_class = ClienteForm

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_list')
