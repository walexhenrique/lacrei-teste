from django.urls import path

from . import views

urlpatterns = [
    path('v1/tarefas/', views.TarefaLista.as_view(), name='tarefas')
]
