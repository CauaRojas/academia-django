from datetime import timedelta

from django.db import models
from django.utils import timezone

"""
Id
Nome
Telefone
email
Dt_matricula
Dt_Nasc
Dt_Venc_mat
"""

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_nascimento = models.DateTimeField()
    data_vencimento_matricula = models.DateTimeField(
        default=timezone.now() + timedelta(days=30))
    foto = models.ImageField(upload_to='fotos/%Y/%m/', blank=True)

    def __str__(self) -> str:
        return self.nome
