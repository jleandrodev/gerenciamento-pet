from django.urls import path
from .views import cliente_views

urlpatterns = [
    path('cadastrar-cliente', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes', cliente_views.listar_clientes, name='lista_clientes'),
    path('clientes/<int:id>', cliente_views.listar_cliente_id, name='cliente_detail'),
    path('editar-cliente/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    path('remover-cliente/<int:id>', cliente_views.remover_cliente, name='remover_cliente')
]