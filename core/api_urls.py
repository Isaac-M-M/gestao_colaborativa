# core/api_urls.py
from rest_framework import routers
from .views import ProjetoViewSet, TarefaViewSet, ComentarioViewSet

router = routers.DefaultRouter()
router.register(r'projetos', ProjetoViewSet)
router.register(r'tarefas', TarefaViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = router.urls
