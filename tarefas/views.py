from django.shortcuts import render
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
