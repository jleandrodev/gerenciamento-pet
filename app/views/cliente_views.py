from django.shortcuts import redirect, render
from ..models import Cliente
from ..forms.cliente_forms import ClienteForm
from ..forms.endereco_forms import EnderecoForm
from ..entidades import cliente, endereco_cliente
from ..services import cliente_service, endereco_service


# Create your views here.

def cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data['nome']
            email = form_cliente.cleaned_data['email']
            cpf = form_cliente.cleaned_data['cpf']
            data_nascimento = form_cliente.cleaned_data['data_nascimento']
            profissao = form_cliente.cleaned_data['profissao']
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data['rua']
                cidade = form_endereco.cleaned_data['cidade']
                estado = form_endereco.cleaned_data['estado']
                endereco_novo = endereco_cliente.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_db = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento, 
                                               profissao=profissao, endereco=endereco_db)
                cliente_service.cadastrar_cliente(cliente_novo)
    else:
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoForm(request.POST)

    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})
