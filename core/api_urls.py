# core/api_urls.py
# Este arquivo define as rotas da API utilizando o Django Rest Framework (DRF).
# Ele cria endpoints automáticos para os ViewSets, permitindo operações CRUD.

from rest_framework import routers
# Importa o sistema de roteamento padrão do DRF,
# que cria URLs automaticamente para ViewSets.

from .views import ProjetoViewSet, TarefaViewSet, ComentarioViewSet
# Importa os ViewSets responsáveis por controlar os endpoints
# de Projetos, Tarefas e Comentários.

# ================================================================
# Criando um roteador padrão do Django REST Framework
# ================================================================
router = routers.DefaultRouter()
# DefaultRouter cria automaticamente:
# - /<endpoint>/   → lista e criação (GET, POST)
# - /<endpoint>/<id>/ → detalhe, edição e exclusão (GET, PUT, PATCH, DELETE)
# Além disso, gera documentação automática na rota raiz quando DEBUG=True.

# ================================================================
# Registrando os endpoints da API
# ================================================================
router.register(r'projetos', ProjetoViewSet)
# Cria todas as rotas de Projetos:
#   GET    /projetos/        → lista
#   POST   /projetos/        → cria
#   GET    /projetos/<id>/   → detalhe
#   PUT    /projetos/<id>/   → atualizar
#   PATCH  /projetos/<id>/   → atualizar parcialmente
#   DELETE /projetos/<id>/   → deletar

router.register(r'tarefas', TarefaViewSet)
# Cria rotas para gerenciamento de Tarefas

router.register(r'comentarios', ComentarioViewSet)
# Cria rotas para gerenciamento de Comentários

# ================================================================
# Exportando todas as URLs geradas automaticamente pelo router
# ================================================================
urlpatterns = router.urls
# urlpatterns agora contém todas as URLs criadas acima.
# Este arquivo geralmente é incluído no urls.py principal do projeto.
