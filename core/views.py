from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm

def projeto_list_view(request):
    projetos = Projeto.objects.all()
    form = ProjetoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('projeto_list')

    return render(request, 'core/projeto_list.html', {'projetos': projetos, 'form': form})

from .models import Comentario
from .forms import ComentarioForm

def comentario_list_view(request):
    comentarios = Comentario.objects.all()
    form = ComentarioForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        comentario = form.save()
        return redirect('comentario_list')

    return render(request, 'core/comentario_list.html', {'comentarios': comentarios, 'form': form})

from .models import Tarefa
from .forms import TarefaForm

def tarefa_list_view(request):
    tarefas = Tarefa.objects.all()
    form = TarefaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('tarefa_list')

    return render(request, 'core/tarefa_list.html', {'tarefas': tarefas, 'form': form})

from django.shortcuts import render

def index_view(request):
    return render(request, 'core/index.html')
