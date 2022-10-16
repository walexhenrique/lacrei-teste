from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tarefa
from .serializers import TarefaSerializer

"""
GET /tarefas/ = Lista todas as tarefas
POST /tarefas/ = Adiciona uma nova tarefa

GET /tarefas/<id>/ = Detalha uma tarefa
PATCH /tarefas/<id>/ = Atualiza uma tarefa
DELETE /tarefas/<id>/ = Apaga uma tarefa
"""

class TarefaLista(APIView):
    """
    Classe responsável pela listagem e criação de novas tarefas
    
    GET /tarefas/ = Lista todas as tarefas
    POST /tarefas/ = Adiciona uma nova tarefa
    """
    def get(self, request):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        data = request.data
        serializer = TarefaSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


class TarefaDetalhe(APIView):
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=200)
