from django.shortcuts import render, redirect
from ..services import funcionario_service
from ..forms import funcionario_form
from ..entidades import funcionario
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required()
def listar_funcionarios(request):
    funcionarios = funcionario_service.listar_funcionarios()
    return render(request, 'funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})


@user_passes_test(lambda f: f.cargo == '2')
def cadastrar_funcionario(request):
    if request.method == 'POST':
        form_funcionario = funcionario_form.FuncionarioForm(request.POST)
        if form_funcionario.is_valid():
            nome = form_funcionario.cleaned_data['nome']
            nascimento = form_funcionario.cleaned_data['nascimento']
            cargo = form_funcionario.cleaned_data['cargo']
            username = form_funcionario.cleaned_data['username']
            password = make_password(form_funcionario.cleaned_data['password1'])

            funcionario_novo = funcionario.Funcionario(nome=nome, nascimento=nascimento, cargo=cargo,
                                                       username=username, password=password)
            funcionario_service.cadastrar_funcionario(funcionario_novo)

            return redirect('lista_funcionarios')
    else:
        form_funcionario = funcionario_form.FuncionarioForm()
    return render(request, 'funcionarios/form_funcionario.html', {'form_funcionario': form_funcionario})
