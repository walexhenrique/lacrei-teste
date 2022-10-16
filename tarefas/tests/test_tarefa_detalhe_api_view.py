import json

from django.urls import reverse
from rest_framework.test import APITestCase

from ..models import Tarefa


class TestObterDetalheTarefa(APITestCase):
    """
    Classe responsável pelos testes do metodo GET ao detalhar tarefa
    """
    
    def setUp(self) -> None:
        self.url = reverse('detalhes', kwargs={'pk': 1})
        return super().setUp()

    def test_tarefa_nao_existe_deve_retornar_404(self):
        """Caso não exista uma tarefa com esse id, retorna status code 404"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 404)

        data = json.loads(response.content)
        self.assertIn('Não encontrado.', data['detail'])

    
    def test_tarefa_detalhe_cadastrada_foi_retornada_com_sucesso(self):
        
        
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


        # Verifica se oque foi apresentado corresponde ao registro da base de dados
        self.assertEqual(data['titulo'], tarefa.titulo)
    
