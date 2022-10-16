from django.shortcuts import render
from rest_framework.views import APIView

from .models import Tarefa


class TarefaLista(APIView):
    def get(self, request):
        ...
