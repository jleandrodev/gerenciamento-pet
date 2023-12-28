from django.shortcuts import redirect, render
from ..forms import consulta_forms
from ..entidades import consulta
from ..services import consulta_service, pet_service
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.loader import render_to_string
from django.core.mail import send_mail

from gerenciamento_pet import settings

@login_required()
def listar_consulta_id(request, id):
    consulta = consulta_service.listar_consulta_id(id)
    return render(request, 'consultas/consulta_detail.html', {'consulta': consulta})


@user_passes_test(lambda u: u.cargo == '1')
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
    

@login_required()
def enviar_email_consulta(request, id):
    consulta = consulta_service.listar_consulta_id(id)
    pet_consulta = pet_service.listar_pet_id(consulta.pet.id)
    assunto = f'Resumo da consulta de {consulta.pet.nome}'

    html_conteudo = render_to_string('consultas/consulta_email.html', {'consulta': consulta})
    corpo_email = 'Resumo da consulta'
    email_remetente = settings.EMAIL_HOST_USER
    email_destino = [pet_consulta.dono.email, ]
    send_mail(assunto, corpo_email, email_remetente, email_destino, html_message=html_conteudo)

    return redirect('consulta_detail', id)
    

        