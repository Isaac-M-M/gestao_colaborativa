from rest_framework import routers
from .views import ProjetoViewSet, TarefaViewSet, ComentarioViewSet
from django.urls import path
from .views import (
    index_view,
    projeto_list_view,
    tarefa_list_view,
    comentario_list_view,
    ProjetoCreateView, ProjetoUpdateView, ProjetoDetailView,
    ProjetoListView, ProjetoDeleteView,
    projeto_create, projeto_update, projeto_detail,
    projeto_list, projeto_delete
)

urlpatterns = [
    path('', index_view, name='index'),
    
    # Views baseadas em função (FBV)
    path('projetos/', projeto_list_view, name='projeto_list'),
    path('tarefas/', tarefa_list_view, name='tarefa_list'),
    path('comentarios/', comentario_list_view, name='comentario_list'),

    # Views baseadas em classe (CBV)
    path('projetos/cbv/', ProjetoListView.as_view(), name='projeto_cbv_listar'),
    path('projetos/cbv/criar/', ProjetoCreateView.as_view(), name='projeto_cbv_criar'),
    path('projetos/cbv/editar/<int:pk>/', ProjetoUpdateView.as_view(), name='projeto_cbv_editar'),
    path('projetos/cbv/<int:pk>/', ProjetoDetailView.as_view(), name='projeto_cbv_detalhar'),
    path('projetos/cbv/deletar/<int:pk>/', ProjetoDeleteView.as_view(), name='projeto_cbv_deletar'),

    # Views baseadas em função (FBV)
    path('projetos/fbv/', projeto_list, name='projeto_fbv_listar'),
    path('projetos/fbv/criar/', projeto_create, name='projeto_fbv_criar'),
    path('projetos/fbv/editar/<int:pk>/', projeto_update, name='projeto_fbv_editar'),
    path('projetos/fbv/<int:pk>/', projeto_detail, name='projeto_fbv_detalhar'),
    path('projetos/fbv/deletar/<int:pk>/', projeto_delete, name='projeto_fbv_deletar'),


]
