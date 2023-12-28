from django.shortcuts import redirect, render
from ..models import Cliente
from ..forms.cliente_forms import ClienteForm
from ..forms.endereco_forms import EnderecoForm
from ..entidades import cliente, endereco_cliente
from ..services import cliente_service, endereco_service, pet_service, consulta_service
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

@login_required()
def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    pets = pet_service.listar_pet_dono(id)
    consultas = consulta_service.listar_consultas_dono(id)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente, 'pets': pets, 'consultas': consultas})

@login_required()
def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    endereco = endereco_service.listar_endereco_id(cliente.endereco.id)
    if request.method == 'POST':
        cliente_service.remover_cliente(cliente)
        endereco_service.remover_endereco(endereco)
        return redirect('lista_clientes')
    return render(request, 'clientes/remover_cliente.html', {'cliente': cliente})

@login_required()
def editar_cliente(request, id):
    cliente_editar = cliente_service.listar_cliente_id(id)
    cliente_editar.data_nascimento = cliente_editar.data_nascimento.strftime('%Y-%m-%d') 
    form_cliente = ClienteForm(request.POST or None, instance=cliente_editar)
    endereco = endereco_service.listar_endereco_id(cliente_editar.endereco.id)
    form_endereco = EnderecoForm(request.POST or None, instance=endereco)

    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data['nome']
        email = form_cliente.cleaned_data['email']
        cpf = form_cliente.cleaned_data['cpf']
        profissao = form_cliente.cleaned_data['profissao']
        data_nascimento = form_cliente.cleaned_data['data_nascimento']
        if form_endereco.is_valid():
            rua = form_endereco.cleaned_data['rua']
            cidade = form_endereco.cleaned_data['cidade']
            estado = form_endereco.cleaned_data['estado']
            endereco_novo = endereco_cliente.Endereco(rua=rua, cidade=cidade, estado=estado)
            endereco_db = endereco_service.editar_endereco(endereco, endereco_novo)
            cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf, data_nascimento=data_nascimento, 
                                            profissao=profissao, endereco=endereco_db)
            cliente_service.editar_cliente(cliente_editar, cliente_novo)
            return redirect('lista_clientes')
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})



    
@login_required()
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
                return redirect('lista_clientes')
    else:
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoForm(request.POST)

    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})

