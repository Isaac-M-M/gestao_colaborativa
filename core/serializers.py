from rest_framework import serializers
# Importa o módulo de serialização do Django Rest Framework (DRF),
# responsável por transformar objetos Python/Django em JSON e vice-versa.

from .models import Projeto, Tarefa, Comentario
# Importa os modelos que serão convertidos em dados JSON para a API.


# ================================================================
# SERIALIZER: Projeto
# ================================================================
class ProjetoSerializer(serializers.ModelSerializer):
    """
    Serializer responsável por converter objetos do model Projeto
    para JSON e também validar dados recebidos em requisições POST/PUT.

    ModelSerializer automatiza a criação dos campos com base no model,
    facilitando o CRUD via API.
    """
    class Meta:
        model = Projeto            # Model associado ao serializer
        fields = '__all__'         # Inclui todos os campos do model


# ================================================================
# SERIALIZER: Tarefa
# ================================================================
class TarefaSerializer(serializers.ModelSerializer):
    """
    Converte objetos Tarefa em JSON e valida dados que chegam pela API.
    Permite criar, editar, listar e excluir tarefas pelo ViewSet correspondente.
    """
    class Meta:
        model = Tarefa             # Model alvo da serialização
        fields = '__all__'         # Usa todos os campos do model 


# ================================================================
# SERIALIZER: Comentario
# ================================================================
class ComentarioSerializer(serializers.ModelSerializer):
    """
    Serializer para comentário. Permite trabalhar com:
    - Conteúdo textual
    - Autores (ManyToMany)
    - Anexo
    - Importância
    - Vínculo com a tarefa

    Também valida uploads e relações durante requisições API.
    """
    class Meta:
        model = Comentario         # Model que será convertido para JSON
        fields = '__all__'         # Inclui todos os campos
