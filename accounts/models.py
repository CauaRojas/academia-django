from django.db import models
from alunos.models import Aluno
from django import forms


class FormAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ('data_criacao',)
# Create your models here.
