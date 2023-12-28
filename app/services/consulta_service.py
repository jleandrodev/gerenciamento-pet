from ..models import ConsultaPet


def cadastrar_consulta(consulta):
    consulta_db = ConsultaPet.objects.create(pet=consulta.pet, motivo=consulta.motivo, 
                    peso_atual=consulta.peso_atual, medicamento_atual=consulta.medicamento_atual,
                    receita=consulta.receita, exames=consulta.exames)
    consulta_db.save()

def listar_consulta_pet(id):
    consultas = ConsultaPet.objects.filter(pet=id).all().order_by('-data')
    return consultas

def listar_consultas_dono(id):
    consultas = ConsultaPet.objects.filter(pet__dono=id).all().order_by('-data')
    return consultas

def listar_consulta_id(id):
    consulta = ConsultaPet.objects.get(id=id)
    return consulta
