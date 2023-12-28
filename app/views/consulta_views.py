from django.shortcuts import redirect, render
from ..forms import consulta_forms
from ..entidades import consulta
from ..services import consulta_service, pet_service

def listar_consulta_id(request, id):
    consulta = consulta_service.listar_consulta_id(id)
    return render(request, 'consultas/consulta_detail.html', {'consulta': consulta})

def cadastrar_consulta(request, id):
    if request.method =='POST':
        form_consulta = consulta_forms.ConsultaPetForm(request.POST)
        pet = pet_service.listar_pet_id(id)
        if form_consulta.is_valid():
            motivo = form_consulta.cleaned_data['motivo']
            peso_atual = form_consulta.cleaned_data['peso_atual']
            medicamento_atual = form_consulta.cleaned_data['medicamento_atual']
            receita = form_consulta.cleaned_data['receita']
            exames = form_consulta.cleaned_data['exames']
            nova_consulta = consulta.ConsultaPet(pet=pet, peso_atual=peso_atual, motivo=motivo, 
                                                 medicamento_atual=medicamento_atual, receita=receita,
                                                 exames=exames)
            consulta_service.cadastrar_consulta(nova_consulta)
            return redirect('pet_detail', pet.id)
    else:
        form_consulta = consulta_forms.ConsultaPetForm()
        return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})
    

        