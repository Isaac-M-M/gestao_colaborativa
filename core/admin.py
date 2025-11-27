from django.contrib import admin
# Importa os modelos que serão exibidos e administrados no Django Admin
from .models import Categoria, Projeto, Equipe, Membro, Tarefa, Comentario

# ================================================
# ADMINISTRAÇÃO DO MODEL: Categoria
# ================================================
@admin.register(Categoria)  # Registra o model Categoria no painel admin
class CategoriaAdmin(admin.ModelAdmin):
    # Campos exibidos na lista de categorias
    list_display = ('nome', 'descricao', 'criada_em', 'ativa', 'prioridade')

    # Permite busca pelo campo nome no topo da página admin
    search_fields = ('nome',)


# ================================================
# ADMINISTRAÇÃO DO MODEL: Projeto
# ================================================
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na listagem do admin
    # "duracao" deve ser um método definido no model Projeto
    list_display = ('titulo', 'categoria', 'data_inicio', 'data_fim', 'duracao')

    # Barra lateral para filtrar por categoria
    list_filter = ('categoria',)


# ================================================
# ADMINISTRAÇÃO DO MODEL: Equipe
# ================================================
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    # Campos de exibição no admin
    list_display = ('nome', 'responsavel', 'projeto', 'setor', 'ativa')

    # Filtro lateral por setor
    list_filter = ('setor',)


# ================================================
# ADMINISTRAÇÃO DO MODEL: Membro
# ================================================
@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    # Colunas mostradas na lista de membros
    list_display = ('nome', 'email', 'funcao', 'equipe', 'data_entrada')

    # Permite buscar por nome ou email
    search_fields = ('nome', 'email')


# ================================================
# ADMINISTRAÇÃO DO MODEL: Tarefa
# ================================================
@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    # Exibe informações completas da tarefa e o método esta_atrasada()
    list_display = ('titulo', 'projeto', 'atribuida_para', 'status', 'prazo', 'esta_atrasada')

    # Filtra tarefas pelo status (ex.: Pendente, Concluída)
    list_filter = ('status',)

    # Campo de busca pelo título
    search_fields = ('titulo',)


# ================================================
# ADMINISTRAÇÃO DO MODEL: Comentario
# ================================================
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    # Exibe tarefa associada, data e se foi editado
    list_display = ('tarefa', 'criado_em', 'editado')
