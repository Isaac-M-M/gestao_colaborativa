from django.urls import path
from .views import projeto_list_view, tarefa_list_view, comentario_list_view
from .views import comentario_list_view
from .views import index_view


urlpatterns = [
    path('projetos/', projeto_list_view, name='projeto_list'),
]


urlpatterns = [
    path('', index_view, name='index'),
    path('projetos/', projeto_list_view, name='projeto_list'),
    path('tarefas/', tarefa_list_view, name='tarefa_list'),
    path('comentarios/', comentario_list_view, name='comentario_list'),
]
