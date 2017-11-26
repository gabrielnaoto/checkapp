from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm, forms, DateField, TextInput

from check.core.models import Cliente, Fornecedor, Banco, Empresa, Emitido, Recebido


class CustomFormHelper(FormHelper):
    form_method = 'post'
    label_class = 'col-lg-2'
    field_class = 'col-lg-12'



    def __init__(self, *args, **kwargs):
        super(CustomFormHelper, self).__init__(*args, **kwargs)
        self.add_input(Submit('submit', 'Salvar'))


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        # fields = '__all__'
        exclude = ['data_cadastro']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()


class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        # fields = '__all__'
        exclude = ['data_cadastro']

    def __init__(self, *args, **kwargs):
        super(FornecedorForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()


class BancoForm(ModelForm):
    class Meta:
        model = Banco
        # fields = '__all__'
        exclude = ['data_cadastro']

    def __init__(self, *args, **kwargs):
        super(BancoForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()


class ChequeEmitidoForm(ModelForm):
    # data_entrada = DateField(widget=TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Emitido
        # fields = '__all__'
        exclude = ['data_cadastro']

    def __init__(self, *args, **kwargs):
        super(ChequeEmitidoForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()


class ChequeRecebidoForm(ModelForm):
    # data_entrada = DateField(widget=TextInput(attrs={'type': 'date'}))
    # data_lancamento = DateField(widget=TextInput(attrs={'type': 'date'}))
    data_desconto = DateField(widget=TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Recebido
        # fields = '__all__'
        exclude = ['data_cadastro', 'tem_fundo', 'foi_repassado', 'foi_compensado']

    def __init__(self, *args, **kwargs):
        super(ChequeRecebidoForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()
