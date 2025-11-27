from rest_framework import routers
# Importação que seria usada para rotas automáticas do Django Rest Framework.
# Neste arquivo, porém, as rotas DRF não estão sendo configuradas aqui
# (a API está em api_urls.py). Esta importação é opcional neste arquivo.

from .views import ProjetoViewSet, TarefaViewSet, ComentarioViewSet
# ViewSets também não estão sendo usados aqui diretamente.
# Foram importados, mas as rotas correspondentes estão em core/api_urls.py.

from django.urls import path
# path é usado para criar rotas no padrão mais moderno do Django.

from .views import (
    index_view,
    projeto_list_view,
    tarefa_list_view,
    comentario_list_view,

    # CBVs (Class-Based Views) para Projeto
    ProjetoCreateView, ProjetoUpdateView, ProjetoDetailView,
    ProjetoListView, ProjetoDeleteView,

    # FBVs (Function-Based Views) para Projeto
    projeto_create, projeto_update, projeto_detail,
    projeto_list, projeto_delete
)
# Importa diversas views da aplicação, incluindo FBVs e CBVs.


# ================================================================
# DEFINIÇÃO DAS ROTAS
# ================================================================
urlpatterns = [
    # ------------------------------------------------------------------
    # ROTA PRINCIPAL (HOME)
    # ------------------------------------------------------------------
    path('', index_view, name='index'),
    # Exibe a página inicial da aplicação.
    # View baseada em função (FBV).

    
    # ------------------------------------------------------------------
    # GRUPO 1 — Views baseadas em função (FBV)
    # Listagens simples
    # ------------------------------------------------------------------
    path('projetos/', projeto_list_view, name='projeto_list'),
    # Lista todos os projetos (versão simples, gerada pelo aluno)

    path('tarefas/', tarefa_list_view, name='tarefa_list'),
    # Lista tarefas sem detalhes avançados

    path('comentarios/', comentario_list_view, name='comentario_list'),
    # Lista comentários sem detalhes avançados


    # ------------------------------------------------------------------
    # GRUPO 2 — Views baseadas em classe (CBV)
    # CRUD completo de Projetos usando classes
    # ------------------------------------------------------------------
    path('projetos/cbv/', ProjetoListView.as_view(), name='projeto_cbv_listar'),
    # Lista todos os projetos usando CBV (ListView)

    path('projetos/cbv/criar/', ProjetoCreateView.as_view(), name='projeto_cbv_criar'),
    # Formulário para criação de projetos (CreateView)

    path('projetos/cbv/editar/<int:pk>/', ProjetoUpdateView.as_view(), name='projeto_cbv_editar'),
    # Edita um projeto específico utilizando UpdateView

    path('projetos/cbv/<int:pk>/', ProjetoDetailView.as_view(), name='projeto_cbv_detalhar'),
    # Detalhes completos de um projeto (DetailView)

    path('projetos/cbv/deletar/<int:pk>/', ProjetoDeleteView.as_view(), name='projeto_cbv_deletar'),
    # Confirmação e exclusão de um projeto (DeleteView)


    # ------------------------------------------------------------------
    # GRUPO 3 — Views baseadas em função (FBV)
    # CRUD completo de Projetos usando funções
    # ------------------------------------------------------------------
    path('projetos/fbv/', projeto_list, name='projeto_fbv_listar'),
    # Lista de projetos usando função

    path('projetos/fbv/criar/', projeto_create, name='projeto_fbv_criar'),
    # Criar projeto usando FBV

    path('projetos/fbv/editar/<int:pk>/', projeto_update, name='projeto_fbv_editar'),
    # Editar projeto via função

    path('projetos/fbv/<int:pk>/', projeto_detail, name='projeto_fbv_detalhar'),
    # Visualizar detalhes do projeto via função

    path('projetos/fbv/deletar/<int:pk>/', projeto_delete, name='projeto_fbv_deletar'),
    # Excluir projeto usando abordagem FBV
]
