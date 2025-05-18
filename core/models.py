from django.db import models
from datetime import date


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)
    prioridade = models.IntegerField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    orcamento = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    @property
    def duracao(self):
        return (self.data_fim - self.data_inicio).days

    def __str__(self):
        return self.titulo


class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)
    setor = models.CharField(max_length=100)
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.nome


class Membro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=100)
    data_entrada = models.DateField()
    telefone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    atribuida_para = models.ForeignKey(Membro, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)
    prazo = models.DateField()
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=50, default="Geral")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    @property
    def esta_atrasada(self):
        return self.prazo < date.today()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Membro)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    editado = models.BooleanField(default=False)
    importancia = models.CharField(max_length=50, default="normal")
    anexo = models.FileField(upload_to='comentarios/', blank=True, null=True)

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        return f"Comentário em {self.tarefa}"
