from django.shortcuts import render, redirect, get_object_or_404
# render   → renderiza templates HTML
# redirect → redireciona para outra URL após alguma ação (ex.: salvar formulário)
# get_object_or_404 → busca um objeto ou retorna erro 404 se não existir

from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
# Importa as views genéricas baseadas em classe (CBV) para implementar CRUD mais rápido.

from django.urls import reverse_lazy
# reverse_lazy → gera URLs a partir do nome da rota (name da URL).
# A versão "lazy" é usada em atributos de classe, pois só é resolvida em tempo de execução.

from rest_framework import viewsets
# viewsets → usado pelo Django Rest Framework para criar APIs baseadas em ModelViewSet.

from .models import Projeto, Tarefa, Comentario
# Importa os models usados nas views.

from .forms import ProjetoForm, TarefaForm, ComentarioForm
# Importa os formulários vinculados aos models.

from .serializers import ProjetoSerializer, TarefaSerializer, ComentarioSerializer
# Importa os serializers usados nas APIs (DRF).


# ================================================================
# VIEW INICIAL (HOME)
# ================================================================
def index_view(request):
    """
    View simples que renderiza a página inicial da aplicação.
    Não envia nenhum contexto especial, apenas exibe o template 'index'.
    """
    return render(request, 'core/index.html')


# ================================================================
# LISTAGEM COM FORMULÁRIO - PROJETOS (FBV)
# ================================================================
def projeto_list_view(request):
    """
    Exibe uma lista de projetos e, ao mesmo tempo,
    permite cadastrar um novo projeto na mesma página.

    - GET: mostra a lista de projetos + formulário em branco.
    - POST: tenta salvar um novo projeto a partir dos dados do formulário.
    """
    # Busca todos os projetos do banco de dados
    projetos = Projeto.objects.all()

    # Cria o formulário com dados do POST (se houver) ou em branco (None)
    form = ProjetoForm(request.POST or None)

    # Se o método for POST, significa que o usuário enviou o formulário
    if request.method == 'POST' and form.is_valid():
        form.save()                     # Salva o novo projeto no banco
        return redirect('projeto_list') # Redireciona para a própria lista

    # Renderiza a página com a lista de projetos e o formulário
    return render(request, 'core/projeto_list.html', {'projetos': projetos, 'form': form})


# ================================================================
# LISTAGEM COM FORMULÁRIO - TAREFAS (FBV)
# ================================================================
def tarefa_list_view(request):
    """
    Exibe uma lista de tarefas e um formulário para criar novas tarefas
    na mesma página.
    """
    tarefas = Tarefa.objects.all()
    form = TarefaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tarefa_list')

    return render(request, 'core/tarefa_list.html', {'tarefas': tarefas, 'form': form})


# ================================================================
# LISTAGEM COM FORMULÁRIO - COMENTÁRIOS (FBV)
# ================================================================
def comentario_list_view(request):
    """
    Exibe uma lista de comentários e permite criar novos comentários
    na mesma tela, incluindo upload de arquivo (anexo).
    """
    comentarios = Comentario.objects.all()

    # request.FILES é necessário para lidar com upload de arquivos (anexo)
    form = ComentarioForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('comentario_list')

    return render(request, 'core/comentario_list.html', {'comentarios': comentarios, 'form': form})


# ================================================================
# CBV — CREATE VIEW (Projeto)
# ================================================================
class ProjetoCreateView(CreateView):
    """
    View baseada em classe para criar projetos usando CreateView.
    Ela gera automaticamente o formulário e trata GET e POST.
    """
    model = Projeto
    # Campos do formulário (selecionados manualmente)
    fields = ['titulo', 'descricao', 'data_inicio', 'orcamento', 'categoria']
    template_name = 'core/projeto_form.html'
    # Após salvar, redireciona para a URL nomeada 'projeto_list'
    success_url = reverse_lazy('projeto_list')


# ================================================================
# CBV — UPDATE VIEW (Projeto)
# ================================================================
class ProjetoUpdateView(UpdateView):
    """
    View baseada em classe para editar um projeto existente.
    Usa o mesmo formulário/template da criação.
    """
    model = Projeto
    fields = ['titulo', 'descricao', 'data_inicio', 'orcamento', 'categoria']
    template_name = 'core/projeto_form.html'
    success_url = reverse_lazy('projeto_list')


# ================================================================
# CBV — DETAIL VIEW (Projeto)
# ================================================================
class ProjetoDetailView(DetailView):
    """
    Exibe os detalhes de um único projeto.
    """
    model = Projeto
    template_name = 'core/projeto_detail.html'


# ================================================================
# CBV — LIST VIEW (Projeto)
# ================================================================
class ProjetoListView(ListView):
    """
    Lista todos os projetos utilizando uma view baseada em classe.
    """
    model = Projeto
    template_name = 'core/projeto_list.html'

    # Nome do contexto no template (em vez de 'object_list')
    context_object_name = 'projetos'


# ================================================================
# CBV — DELETE VIEW (Projeto)
# ================================================================
class ProjetoDeleteView(DeleteView):
    """
    Exibe uma página de confirmação e exclui um projeto
    ao confirmar o formulário (POST).
    """
    model = Projeto
    template_name = 'core/projeto_confirm_delete.html'
    success_url = reverse_lazy('projeto_list')


# ================================================================
# FBV — CREATE (Projeto)
# ================================================================
def projeto_create(request):
    """
    Cria um projeto utilizando uma view baseada em função (FBV).

    - GET: exibe o formulário em branco.
    - POST: processa e salva o formulário, se válido.
    """
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projeto_list')
    else:
        form = ProjetoForm()

    return render(request, 'core/projeto_form.html', {'form': form})


# ================================================================
# FBV — UPDATE (Projeto)
# ================================================================
def projeto_update(request, pk):
    """
    Edita um projeto existente (FBV).
    Recebe o ID (pk) do projeto na URL.
    """
    # Busca o projeto ou retorna 404 se não existir
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto_list')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'core/projeto_form.html', {'form': form})


# ================================================================
# FBV — DETAIL (Projeto)
# ================================================================
def projeto_detail(request, pk):
    """
    Exibe os detalhes de um projeto específico utilizando FBV.
    """
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'core/projeto_detail.html', {'projeto': projeto})


# ================================================================
# FBV — LIST (Projeto)
# ================================================================
def projeto_list(request):
    """
    Lista todos os projetos (versão simples, sem formulário embutido).
    """
    projetos = Projeto.objects.all()
    return render(request, 'core/projeto_list.html', {'projetos': projetos})


# ================================================================
# FBV — DELETE (Projeto)
# ================================================================
def projeto_delete(request, pk):
    """
    Exclui um projeto após confirmação via POST.
    - GET: mostra a página de confirmação de exclusão.
    - POST: de fato exclui o projeto e redireciona.
    """
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        return redirect('projeto_list')

    return render(request, 'core/projeto_confirm_delete.html', {'projeto': projeto})


# ================================================================
# API — VIEWSETS (Django REST Framework)
# ================================================================
class ProjetoViewSet(viewsets.ModelViewSet):
    """
    API REST para Projeto.
    ModelViewSet já implementa:
    - list   (GET /projetos/)
    - create (POST /projetos/)
    - retrieve (GET /projetos/<id>/)
    - update / partial_update (PUT/PATCH)
    - destroy (DELETE)
    """
    queryset = Projeto.objects.all()         # Conjunto de dados da API
    serializer_class = ProjetoSerializer     # Converte Projeto ↔ JSON


class TarefaViewSet(viewsets.ModelViewSet):
    """
    API REST para Tarefa, com operações CRUD completas.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    """
    API REST para Comentario.
    Permite trabalhar com comentários, incluindo autores e anexos via API.
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
