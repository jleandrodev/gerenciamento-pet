from ..models import ConsultaPet


def cadastrar_consulta(consulta):
    consulta_db = ConsultaPet.objects.create(pet=consulta.pet, motivo=consulta.motivo, 
                    peso_atual=consulta.peso_atual, medicamento_atual=consulta.medicamento_atual,
                    receita=consulta.receita, exames=consulta.exames)
    consulta_db.save()

def listar_consulta_pet(id):
    consultas = ConsultaPet.objects.filter(pet=id)
    return consultas
