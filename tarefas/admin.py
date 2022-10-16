from django.contrib import admin

from .models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_e_hora_de_criacao', 'ultima_modificacao', 'finalizado',)
    list_display_links = ('titulo',)
    list_editable = ('finalizado',)
    list_filter = ('id', 'titulo', 'finalizado',)
