from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:aluno_id>", views.aluno, name="aluno"),
    path('tempo/<int:id>', views.add_tempo, name='add_tempo'),
    path('busca/', views.busca, name='busca'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
]
