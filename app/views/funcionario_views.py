from django.shortcuts import render, redirect
from ..services import funcionario_service
from ..forms import funcionario_form
from ..entidades import funcionario

def listar_funcionarios(request):
    funcionarios = funcionario_service.listar_funcionarios()
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})

def cadastrar_funcionario(request):
    if request.method == 'POST':
        form_funcionario = funcionario_form.FuncionarioForm(request.POST)
        if form_funcionario.is_valid():
            nome = form_funcionario.cleaned_data['nome']
            nascimento = form_funcionario.cleaned_data['nascimento']
            cargo = form_funcionario.cleaned_data['cargo']

            funcionario_novo = funcionario.Funcionario(nome=nome, nascimento=nascimento, cargo=cargo)
            funcionario_service.cadastrar_funcionario(funcionario_novo)

            return redirect('lista_funcionarios')
    else:
        form_funcionario = funcionario_form.FuncionarioForm()
    return render(request, 'funcionarios/form_funcionario.html', {'form_funcionario': form_funcionario})
