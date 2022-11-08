from django.contrib import admin
from .models import Aluno
# Register your models here.


class AlunoAdm(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email', 'data_criacao',
                    'data_nascimento', 'data_vencimento_matricula')
    list_display_links = ('id', 'nome', 'telefone')
    list_filter = ('data_criacao',)
    list_per_page = (10)
    search_fields = ('nome', 'telefone', 'email', 'data_vencimento_matricula')
    list_editable = ('data_vencimento_matricula',)

admin.site.register(Aluno, AlunoAdm)
