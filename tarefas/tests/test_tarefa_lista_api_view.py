import json

from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import Tarefa


class TestListagemTarefas(APITestCase):
    """
    Classe responsável pelos testes essenciais da API na funcionalidade de listagem
    """
    
    def setUp(self) -> None:
        self.url = reverse('tarefas')
        return super().setUp()

    def test_listagem_tarefas_vazia(self):
        """Caso não tenha sido realizado nenhum cadastro de tarefa, deve retornar uma lista vazia"""
        response = self.client.get(self.url)

        data = json.loads(response.content)
        self.assertEqual([], data)

    def test_listagem_de_tarefas_cadastradas_sao_retornadas_com_sucesso(self):
        """Checka se as tarefas estão sendo retornadas de forma correta"""
        
        # Criando uma tarefa

        tarefa = Tarefa.objects.create(
            titulo='Tarefa 1',
            descricao = 'Descricao tarefa 1',
            finalizado = True
        )

        response = self.client.get(self.url)
        data = json.loads(response.content)

        # Verifica se tudo ocorreu bem
        self.assertEqual(response.status_code, 200)

        # Verifica o tamanho das listagem de tarefas cadastradas
        self.assertEqual(len(data), 1)

        # Verifica se oque foi apresentado corresponde ao registro da base de dados
        self.assertEqual(data[0]['titulo'], tarefa.titulo)


class TestCriacaoTarefa(APITestCase):
    """
    Classe responsável pelos testes de criação de novas tarefas
    """
    def setUp(self) -> None:
        self.url = reverse('tarefas')
        return super().setUp()
    
    def test_cria_tarefa_com_sucesso(self):
        request_data = {
            "titulo": "Tarefa 1",
            "descricao": "Descricao tarefa 1"
        }
        response = self.client.post(self.url, data=request_data, format='json')
        
        # Verifica se retornou o status code 201 indicando que tudo ocorreu bem
        self.assertEqual(response.status_code, 201)

        tarefa = Tarefa.objects.get(pk=1)

        # Verifica se o atributo foi criado de forma correta de acordo com a minha requisição json
        self.assertEqual(tarefa.titulo, request_data['titulo'])
    
    def test_tentar_criar_uma_tarefa_sem_titulo_nao_deve_ser_possivel(self):

        request_data = {
            "descricao": "Descricao tarefa 1"
        }

        response = self.client.post(self.url, data=request_data, format='json')

        # Verifica se retornou o status code 400 indicando que ocorreu um erro na criação do objeto
        self.assertEqual(response.status_code, 400)

        # Nenhuma tarefa deve ter sido criada
        tarefas_criadas = Tarefa.objects.all()
        self.assertEqual(len(tarefas_criadas), 0)
    
    def test_tentar_criar_uma_tarefa_sem_descricao_nao_deve_ser_possivel(self):

        request_data = {
            "titulo": "Tarefa 1"
        }

        response = self.client.post(self.url, data=request_data, format='json')

        # Verifica se retornou o status code 400 indicando que ocorreu um erro na criação do objeto
        self.assertEqual(response.status_code, 400)

        # Nenhuma tarefa deve ter sido criada
        tarefas_criadas = Tarefa.objects.all()
        self.assertEqual(len(tarefas_criadas), 0)
