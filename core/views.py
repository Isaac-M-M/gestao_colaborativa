from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy

from .models import Projeto, Tarefa, Comentario
from .forms import ProjetoForm, TarefaForm, ComentarioForm

# Página inicial
def index_view(request):
    return render(request, 'core/index.html')


# ----------------------------
# PROJETO - VIEW BASEADA EM FUNÇÃO (FBV)
# ----------------------------

def projeto_list_view(request):
    projetos = Projeto.objects.all()
    form = ProjetoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('projeto_list')
    return render(request, 'core/projeto_list.html', {'projetos': projetos, 'form': form})


# ----------------------------
# TAREFA - VIEW BASEADA EM FUNÇÃO
# ----------------------------

def tarefa_list_view(request):
    tarefas = Tarefa.objects.all()
    form = TarefaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tarefa_list')
    return render(request, 'core/tarefa_list.html', {'tarefas': tarefas, 'form': form})


# ----------------------------
# COMENTÁRIO - VIEW BASEADA EM FUNÇÃO
# ----------------------------

def comentario_list_view(request):
    comentarios = Comentario.objects.all()
    form = ComentarioForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('comentario_list')
    return render(request, 'core/comentario_list.html', {'comentarios': comentarios, 'form': form})


# ----------------------------
# PROJETO - VIEWS BASEADAS EM CLASSE (CBV)
# ----------------------------

class ProjetoCreateView(CreateView):
    model = Projeto
    fields = ['titulo', 'descricao', 'data_inicio', 'orcamento', 'categoria']
    template_name = 'core/projeto_form.html'
    success_url = reverse_lazy('projeto_list')

class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = ['titulo', 'descricao', 'data_inicio', 'orcamento', 'categoria']
    template_name = 'core/projeto_form.html'
    success_url = reverse_lazy('projeto_list')

class ProjetoDetailView(DetailView):
    model = Projeto
    template_name = 'core/projeto_detail.html'

class ProjetoListView(ListView):
    model = Projeto
    template_name = 'core/projeto_list.html'
    context_object_name = 'projetos'

class ProjetoDeleteView(DeleteView):
    model = Projeto
    template_name = 'core/projeto_confirm_delete.html'
    success_url = reverse_lazy('projeto_list')


# ----------------------------
# PROJETO - VIEWS BASEADAS EM FUNÇÃO (FBV)
# ----------------------------

def projeto_create(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projeto_list')
    else:
        form = ProjetoForm()
    return render(request, 'core/projeto_form.html', {'form': form})

def projeto_update(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto_list')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'core/projeto_form.html', {'form': form})

def projeto_detail(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'core/projeto_detail.html', {'projeto': projeto})

def projeto_list(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/projeto_list.html', {'projetos': projetos})

def projeto_delete(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('projeto_list')
    return render(request, 'core/projeto_confirm_delete.html', {'projeto': projeto})
