from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Projeto, Tarefa, Comentario
from .forms import ProjetoForm, TarefaForm, ComentarioForm
from .serializers import ProjetoSerializer, TarefaSerializer, ComentarioSerializer


def index_view(request):
    return render(request, 'core/index.html')


def projeto_list_view(request):
    projetos = Projeto.objects.all()
    form = ProjetoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('projeto_list')
    return render(request, 'core/projeto_list.html', {'projetos': projetos, 'form': form})


def tarefa_list_view(request):
    tarefas = Tarefa.objects.all()
    form = TarefaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tarefa_list')
    return render(request, 'core/tarefa_list.html', {'tarefas': tarefas, 'form': form})


def comentario_list_view(request):
    comentarios = Comentario.objects.all()
    form = ComentarioForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('comentario_list')
    return render(request, 'core/comentario_list.html', {'comentarios': comentarios, 'form': form})


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


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
