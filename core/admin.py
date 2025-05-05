from django.contrib import admin
from .models import Categoria, Projeto, Equipe, Membro, Tarefa, Comentario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'criada_em', 'ativa', 'prioridade')
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_inicio', 'data_fim', 'duracao')
    list_filter = ('categoria',)

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'responsavel', 'projeto', 'setor', 'ativa')
    list_filter = ('setor',)

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'funcao', 'equipe', 'data_entrada')
    search_fields = ('nome', 'email')

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'atribuida_para', 'status', 'prazo', 'esta_atrasada')
    list_filter = ('status',)
    search_fields = ('titulo',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'criado_em', 'editado')
