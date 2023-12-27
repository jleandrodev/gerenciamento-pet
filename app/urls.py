from django.urls import path
from .views import cliente_views

urlpatterns = [
    path('cadastrar-cliente', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('listar-clientes', cliente_views.listar_clientes, name='lista_clientes')
]