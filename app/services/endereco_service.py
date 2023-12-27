from ..models import EnderecoCliente

def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)

def listar_endereco_id(id):
    return EnderecoCliente.objects.get(id=id)

def editar_endereco(endereco, endereco_novo):
    endereco.rua = endereco_novo.rua
    endereco.cidade = endereco_novo.cidade
    endereco.estado = endereco_novo.estado
    endereco.save(force_update=True)
    return endereco

def remover_endereco(endereco):
    endereco.delete()
