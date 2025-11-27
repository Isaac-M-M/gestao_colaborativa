from django import forms
# Importa o módulo de formulários do Django, que permite criar formulários
# HTML automaticamente baseados em classes Python.

from .models import Projeto, Tarefa, Comentario
# Importa os modelos que serão associados aos formulários.


# ================================================================
# FORMULÁRIO DE PROJETO
# ================================================================
class ProjetoForm(forms.ModelForm):
    """
    Formulário baseado no model Projeto.
    ModelForm gera automaticamente todos os campos do formulário
    com base nos campos definidos no model correspondente.
    """
    class Meta:
        # Define qual model o formulário representa
        model = Projeto
        
        # '__all__' indica que todos os campos do model serão incluídos no formulário
        fields = '__all__'


# ================================================================
# FORMULÁRIO DE TAREFA
# ================================================================
class TarefaForm(forms.ModelForm):
    """
    Formulário baseado no model Tarefa.
    Permite criar e editar tarefas utilizando os campos definidos no model.
    """
    class Meta:
        model = Tarefa   # Model alvo
        fields = '__all__'  # Inclui todos os campos disponíveis


# ================================================================
# FORMULÁRIO DE COMENTÁRIO
# ================================================================
class ComentarioForm(forms.ModelForm):
    """
    Formulário baseado no model Comentario.
    Inclui campos como conteúdo, autores, anexo e data de criação.
    """
    class Meta:
        model = Comentario  # Model associado ao formulário
        fields = '__all__'  # Campos completos do model
