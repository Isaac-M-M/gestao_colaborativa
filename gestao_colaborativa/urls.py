from django.contrib import admin
# Importa o módulo responsável pelo painel administrativo do Django.

from django.urls import path, include
# path → usado para criar roteamento simples.
# include → permite incluir outros arquivos de urls dentro deste arquivo principal.

from rest_framework import routers
# Importa o roteador do Django Rest Framework para gerar rotas automáticas.

from core.views import ProjetoViewSet
# Importa o ViewSet de Projeto para criar rotas da API.
# (Os demais ViewSets estão em core/api_urls.py, mas aqui você registrou apenas Projeto.)


# ================================================================
# ROTEAMENTO DA API REST (DRF)
# ================================================================
router = routers.DefaultRouter()
# Cria um roteador padrão que gera rotas automáticas para ViewSets.

router.register(r'api/projetos', ProjetoViewSet)
# Registra o endpoint /api/projetos/
# Gera automaticamente:
#   GET    /api/projetos/        → lista projetos
#   POST   /api/projetos/        → cria projeto
#   GET    /api/projetos/<id>/   → detalhe
#   PUT    /api/projetos/<id>/   → atualizar
#   PATCH  /api/projetos/<id>/   → atualizar parcialmente
#   DELETE /api/projetos/<id>/   → excluir


# ================================================================
# URLS PRINCIPAIS DO PROJETO
# ================================================================
urlpatterns = [
    # Painel administrativo padrão do Django
    path('admin/', admin.site.urls),

    # Inclui todas as rotas da aplicação 'core'
    # Essas rotas incluem:
    #   - /                (index)
    #   - /projetos/       (FBV)
    #   - /projetos/cbv/   (CBV)
    #   - /tarefas/
    #   - /comentarios/
    path('', include('core.urls')),

    # Inclui as rotas geradas automaticamente pelo router DRF
    # Essas rotas serão adicionadas ao caminho base ''
    path('', include(router.urls)),
]
