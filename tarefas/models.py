from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    data_e_hora_de_criacao = models.DateTimeField(auto_now_add=True)
    ultima_modificacao = models.DateTimeField(auto_now=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo
    
