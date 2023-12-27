from django.urls import path
from .views import cliente_views, pet_views

urlpatterns = [
    path('cadastrar-cliente', cliente_views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes', cliente_views.listar_clientes, name='lista_clientes'),
    path('clientes/<int:id>', cliente_views.listar_cliente_id, name='cliente_detail'),
    path('editar-cliente/<int:id>', cliente_views.editar_cliente, name='editar_cliente'),
    path('remover-cliente/<int:id>', cliente_views.remover_cliente, name='remover_cliente'),
    path('cadastrar-pet/<int:id>', pet_views.cadastrar_pet, name='cadastrar_pet' ),
    path('pets', pet_views.listar_pets, name='lista_pets'),
    path('pets/<int:id>', pet_views.listar_pet_id, name='pet_detail'),
    path('editar-pet/<int:id>', pet_views.editar_pet, name='editar_pet')
]