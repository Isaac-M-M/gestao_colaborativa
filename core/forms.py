from django import forms
from .models import Projeto, Tarefa, Comentario

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
