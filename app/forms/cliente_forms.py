from django import forms
from ..models import Cliente
from django.forms import DateInput

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'data_nascimento', 'cpf', 'profissao']
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': 'date'}
            )
        }