from rest_framework import serializers

from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ('id', 'titulo', 'descricao', 'data_e_hora_de_criacao', 'ultima_modificacao', 'finalizado',)
