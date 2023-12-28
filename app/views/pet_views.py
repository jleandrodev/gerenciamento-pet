from django.shortcuts import render, redirect
from ..forms import pet_forms
from ..entidades import pet
from ..services import cliente_service, pet_service, consulta_service
from django.contrib.auth.decorators import login_required


@login_required()
def cadastrar_pet(request, id):
    if request.method == 'POST':
        form_pet = pet_forms.PetForm(request.POST)
        dono = cliente_service.listar_cliente_id(id)

        if form_pet.is_valid():
            nome = form_pet.cleaned_data['nome']
            nascimento = form_pet.cleaned_data['nascimento']
            categoria = form_pet.cleaned_data['categoria']
            cor = form_pet.cleaned_data['cor']

            pet_novo = pet.Pet(nome=nome, nascimento=nascimento, categoria=categoria, cor=cor, dono=dono)
            pet_service.cadastrar_pet(pet_novo)
            return redirect('lista_clientes')
    else:
        form_pet = pet_forms.PetForm()
    return render(request, 'pets/form_pet.html', {'form_pet': form_pet})


@login_required()
def listar_pets(request):
    pets = pet_service.listar_pets()
    return render(request, 'pets/lista_pets.html', {'pets': pets})


@login_required()
def listar_pet_id(request, id):
    pet = pet_service.listar_pet_id(id)
    consultas = consulta_service.listar_consulta_pet(id)
    return render(request, 'pets/pet_detail.html', {'pet': pet, 'consultas': consultas})


@login_required()
def editar_pet(request, id):
    pet_antigo = pet_service.listar_pet_id(id)
    pet_antigo.nascimento = pet_antigo.nascimento.strftime('%Y-%m-%d') 
    form_pet = pet_forms.PetForm(request.POST or None, instance=pet_antigo)

    if form_pet.is_valid():
        nome = form_pet.cleaned_data['nome']
        nascimento = form_pet.cleaned_data['nascimento']
        categoria = form_pet.cleaned_data['categoria']
        cor = form_pet.cleaned_data['cor']
        dono = pet_antigo.dono

        pet_novo = pet.Pet(dono=dono, nome=nome, nascimento=nascimento, categoria=categoria, cor=cor)

        pet_service.editar_pet(pet_antigo, pet_novo)
        return redirect('lista_pets')
    return render(request, 'pets/form_pet.html', {'form_pet': form_pet})