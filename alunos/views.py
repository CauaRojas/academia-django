from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from datetime import timedelta
from datetime import datetime


def index(request):

    alunos = Aluno.objects.order_by('-data_criacao')
    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)
    return render(request, 'alunos/index.html', {
        'alunos': alunos,
    })


def aluno(request, aluno_id):
    #aluno = Aluno.objects.get(id=aluno_id)
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if aluno.data_vencimento_matricula.timestamp() < datetime.now().timestamp():
        messages.add_message(request, messages.ERROR,
                             'Matrícula vencida')
    return render(request, 'alunos/detalhes.html', {
        'aluno': aluno
    })


def busca(request):
    q = request.GET.get('q')
    if q is None or not q:
        messages.add_message(request, messages.ERROR,
                             'Digite algo para buscar')
        return redirect('index')
    alunos = Aluno.objects.order_by('-data_criacao').filter(Q(nome__icontains=q) | Q(telefone__icontains=q) | Q(email__icontains=q) | Q(
        data_nascimento__icontains=q) | Q(data_vencimento_matricula__icontains=q) | Q(data_criacao__icontains=q) | Q(id__icontains=q))
    paginator = Paginator(alunos, 10)
    page = request.GET.get('page')
    alunos = paginator.get_page(page)

    return render(request, 'alunos/busca.html', {
        'alunos': alunos,
    })


def add_tempo(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.data_vencimento_matricula = aluno.data_vencimento_matricula + \
        timedelta(days=30)
    aluno.save()
    return redirect('aluno', aluno_id=id)


def deletar(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('index')
