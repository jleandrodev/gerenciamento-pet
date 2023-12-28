from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from django.contrib.auth.models import AbstractUser

# Create your models here.

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES, null=False, blank=False)

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    profissao = models.CharField(max_length=30, null=False, blank=False)

class Pet(models.Model):
    CATEGORIA_PET_CHOICES = (
        ('ca', 'Cachorro'),
        ('ga', 'Gato'),
        ('co', 'Coelho'),
        ('ta', 'Tartaruga'),
        ('pa', 'Pássaro'),
    )

    COR_PET_CHOICES = (
        ('pr', 'Preto'),
        ('br', 'Branco'),
        ('ci', 'Cinza'),
        ('ma', 'Marrom'),
    )

    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_PET_CHOICES, null=False, blank=False)
    cor = models.CharField(max_length=2, choices=COR_PET_CHOICES, null=False, blank=False)
    dono = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False)


class ConsultaPet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    motivo = models.CharField(max_length=200, null=False, blank=False)
    peso_atual = models.FloatField(null=False, blank=False)
    medicamento_atual = models.TextField(null=False, blank=True)
    receita = models.TextField(null=False, blank=True)
    exames = models.TextField(null=False, blank=True)

class Funcionario(AbstractUser):
    CARGO_CHOICES = (
        ('1', 'Veterinário'),
        ('2', 'Financeiro'),
        ('3', 'Atendente'),
    )
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    cargo = models.CharField(max_length=1, choices=CARGO_CHOICES, null=False, blank=False)

