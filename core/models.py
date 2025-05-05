from django.db import models
from datetime import date

class Categoria(models.Model):
    nome = models.CharField(max_length=100)  # Campo de texto limitado a 100 caracteres
    descricao = models.TextField()  # Campo de texto sem limite definido
    criada_em = models.DateTimeField(auto_now_add=True)  # Registra data/hora automática ao criar
    ativa = models.BooleanField(default=True)  # Indica se a categoria está ativa
    prioridade = models.IntegerField()  # Número indicando prioridade

    class Meta:
        verbose_name = "Categoria"  # Nome no singular no admin
        verbose_name_plural = "Categorias"  # Nome plural no admin

    def __str__(self):
        return self.nome  # Exibição do objeto no admin


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)  # Nome do projeto
    descricao = models.TextField()  # Detalhes do projeto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relacionado à uma categoria
    data_inicio = models.DateField()  # Início do projeto
    data_fim = models.DateField()  # Fim do projeto
    orcamento = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do projeto

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    @property
    def duracao(self):
        return (self.data_fim - self.data_inicio).days  # Calcula a duração em dias

    def __str__(self):
        return self.titulo


class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)  # Nome da pessoa responsável
    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)  # Relação 1:1 com o projeto
    setor = models.CharField(max_length=100)  # Área ou departamento
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True)  # Campo opcional para anotações

    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.nome


class Membro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()  # Campo especializado para e-mail
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)  # Muitos membros por equipe
    funcao = models.CharField(max_length=100)  # Cargo ou papel na equipe
    data_entrada = models.DateField()
    telefone = models.CharField(max_length=20, blank=True)  # Campo opcional

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)  # Tarefa ligada a um projeto
    atribuida_para = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True)  # Se o membro for apagado, vira NULL
    status = models.CharField(max_length=50)  # Ex: "Pendente", "Concluído"
    prazo = models.DateField()
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=50, default="Geral")  # Ex: "Desenvolvimento", "Testes"

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    @property
    def esta_atrasada(self):
        return self.prazo < date.today()  # Verifica se a data limite já passou

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)  # Cada comentário pertence a uma tarefa
    autores = models.ManyToManyField(Membro)  # Um ou mais autores podem comentar
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    editado = models.BooleanField(default=False)  # Indica se o comentário foi editado
    importancia = models.CharField(max_length=50, default="normal")  # Nível de importância
    anexo = models.FileField(upload_to='comentarios/', blank=True, null=True)  # Upload opcional de arquivo

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        return f"Comentário em {self.tarefa}"
