from django.urls import path

from . import views

urlpatterns = [
    path('v1/tarefas/', views.TarefaLista.as_view(), name='tarefas'),
    path('v1/tarefas/<int:pk>/', views.TarefaDetalhe.as_view(), name='detalhes'),
]
