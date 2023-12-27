from django import forms
from ..models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'nascimento', 'categoria', 'cor']
        exclude = ['dono', ]
        widgets = {
            'nascimento': forms.DateInput(
                attrs={'type': 'date'}
            )
        }