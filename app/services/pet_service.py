from ..models import Pet

def cadastrar_pet(pet):
    pet_db = Pet.objects.create(nome=pet.nome, nascimento=pet.nascimento, 
            categoria=pet.categoria, cor=pet.cor, dono=pet.dono)
    pet_db.save()

def listar_pets():
    return Pet.objects.all()

def listar_pet_dono(id):
    pets = Pet.objects.filter(dono=id).all()
    return pets

def editar_pet(pet, pet_novo):
    pet.nome = pet_novo.nome
    pet.nascimento = pet_novo.nascimento
    pet.categoria = pet_novo.categoria
    pet.cor = pet_novo.cor
    pet.dono = pet_novo.dono

    pet.save(force_update=True)


def listar_pet_id(id):
    pet = Pet.objects.get(id=id)
    return pet
