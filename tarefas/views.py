from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tarefa
from .serializers import TarefaSerializer


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
    """
    Classe responsável por detalhar uma tarefa, 
    
    Métodos disponíveis:
    
    GET /tarefas/<id>/ = Detalha a tarefa
    PATCH /tarefas/<id>/ = Atualiza a tarefa
    DELETE /tarefas/<id>/ = Apaga a tarefa
    """
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=200)
    
    def patch(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        serializer = TarefaSerializer(tarefa, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        tarefa.delete()
        return Response(status=204)
    
