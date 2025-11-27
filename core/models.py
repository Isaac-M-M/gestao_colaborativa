from django.db import models
from datetime import date
# Importa o módulo de modelos do Django e o objeto date
# que permite trabalhar com datas no Python.


# ================================================================
# MODELO: Categoria
# ================================================================
class Categoria(models.Model):
    # Nome da categoria (ex.: "Urgente", "Financeiro", "Infraestrutura")
    nome = models.CharField(max_length=100)

    # Descrição detalhada da categoria
    descricao = models.TextField()

    # Data/hora em que a categoria foi criada (registrada automaticamente)
    criada_em = models.DateTimeField(auto_now_add=True)

    # Campo booleano para ativar/desativar categoria sem excluir do sistema
    ativa = models.BooleanField(default=True)

    # Número que indica prioridade da categoria (menor = mais prioritária)
    prioridade = models.IntegerField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    # Representação do objeto no painel admin ou em textos
    def __str__(self):
        return self.nome


# ================================================================
# MODELO: Projeto
# ================================================================
class Projeto(models.Model):
    # Título do projeto (ex.: "Sistema de Gestão")
    titulo = models.CharField(max_length=200)

    # Descrição completa do projeto
    descricao = models.TextField()

    # Relação: um projeto pertence a uma única categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Datas de início e fim do projeto
    data_inicio = models.DateField()
    data_fim = models.DateField()

    # Valor total do orçamento do projeto (até 99999999.99)
    orcamento = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    # Propriedade calculada automaticamente
    # Retorna a quantidade de dias entre início e fim
    @property
    def duracao(self):
        return (self.data_fim - self.data_inicio).days

    def __str__(self):
        return self.titulo


# ================================================================
# MODELO: Equipe
# ================================================================
class Equipe(models.Model):
    # Nome da equipe (ex.: "Desenvolvimento", "Marketing")
    nome = models.CharField(max_length=100)

    # Pessoa responsável pela equipe
    responsavel = models.CharField(max_length=100)

    # Relação OneToOne: cada projeto possui UMA equipe principal
    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)

    # Setor ao qual a equipe pertence
    setor = models.CharField(max_length=100)

    # A equipe está ativa? (pode ser desativada sem ser excluída)
    ativa = models.BooleanField(default=True)

    # Quando a equipe foi registrada no sistema
    criada_em = models.DateTimeField(auto_now_add=True)

    # Campo livre para observações gerais
    observacoes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.nome


# ================================================================
# MODELO: Membro
# ================================================================
class Membro(models.Model):
    # Nome completo do membro
    nome = models.CharField(max_length=100)

    # Email para contato
    email = models.EmailField()

    # Relação: vários membros pertencem a uma equipe
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    # Função desempenhada (ex.: "Desenvolvedor", "Gerente", "Tester")
    funcao = models.CharField(max_length=100)

    # Data em que o membro começou na equipe
    data_entrada = models.DateField()

    # Telefone opcional do membro
    telefone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __str__(self):
        return self.nome


# ================================================================
# MODELO: Tarefa
# ================================================================
class Tarefa(models.Model):
    # Título da tarefa (ex.: "Criar API de Projetos")
    titulo = models.CharField(max_length=200)

    # Relação: tarefa pertence a um projeto
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    # Membro responsável pela tarefa (opcional)
    atribuida_para = models.ForeignKey(
        Membro,
        on_delete=models.SET_NULL,
        null=True
    )

    # Status atual da tarefa (ex.: "Pendente", "Em andamento", "Concluída")
    status = models.CharField(max_length=50)

    # Prazo final para conclusão
    prazo = models.DateField()

    # Descrição detalhada (opcional)
    descricao = models.TextField(blank=True)

    # Tipo da tarefa (categoria interna)
    tipo = models.CharField(max_length=50, default="Geral")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    # Verifica automaticamente se a tarefa está atrasada
    @property
    def esta_atrasada(self):
        return self.prazo < date.today()

    def __str__(self):
        return self.titulo


# ================================================================
# MODELO: Comentario
# ================================================================
class Comentario(models.Model):
    # Relação: um comentário está associado a uma tarefa específica
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)

    # Um comentário pode ter vários autores (ex.: revisão conjunta)
    autores = models.ManyToManyField(Membro)

    # Texto do comentário
    conteudo = models.TextField()

    # Data em que foi criado (gerada automaticamente)
    criado_em = models.DateTimeField(auto_now_add=True)

    # Indica se o comentário foi alterado após criado
    editado = models.BooleanField(default=False)

    # Nível de importância (ex.: "normal", "urgente", "aviso")
    importancia = models.CharField(max_length=50, default="normal")

    # Anexo opcional (arquivos são enviados para MEDIA_ROOT/comentarios/)
    anexo = models.FileField(upload_to='comentarios/', blank=True, null=True)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        # Retorna informação legível, mesclando comentário e tarefa
        return f"Comentário em {self.tarefa}"
