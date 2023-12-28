from ..models import Funcionario

def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(nome=funcionario.nome, nascimento=funcionario.nascimento, 
                               cargo=funcionario.cargo)
    
def listar_funcionarios():
    funcionarios = Funcionario.objects.all()
    return funcionarios
