from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from check.core.models import Cliente


class CustomFormHelper(FormHelper):
    form_method = 'post'
    form_class = 'form-horizontal'
    label_class = 'col-lg-2'
    field_class = 'col-lg-8'

    def __init__(self, *args, **kwargs):
        super(CustomFormHelper, self).__init__(*args, **kwargs)
        self.add_input(Submit('submit', 'Salvar'))


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.helper = CustomFormHelper()
