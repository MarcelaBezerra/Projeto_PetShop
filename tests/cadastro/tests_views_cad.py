from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Cadastro
from .views import processa_cadastro


class CadastroTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.cadastro_data = {
            'CAD_NOME': 'João',
            'CAD_EMAIL': 'joaoexample.com',
            'CAD_RUA': 'rua 123',
            'CAD_NUMERO': '123',
            'CAD_BAIRRO': 'Bairro123',
            'CAD_CIDADE': 'City123',
            'CAD_CONTATO': '123456789',
            'CAD_SENHA': '12345'
        }

    def test_processa_cadastro_missing_fields(self):
        # Testar quando campos obrigatórios estão faltando
        # Ele verifica se a view redireciona para a URL correta com um parâmetro indicando
        # o erro e garante que nenhum cadastro seja salvo no banco de dados.
        incomplete_data = self.cadastro_data.copy()
        incomplete_data['CAD_NOME'] = ''

        url = reverse('processa_cadastro')
        request = self.factory.post(url, data=incomplete_data)
        response = processa_cadastro(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cadastro/?status=3')

    def test_processa_cadastro_invalid_data(self):
        # Testar quando os campos possuem dados inválidos
        # Ele verifica se a view redireciona para a URL correta 
        # com um parâmetro indicando o erro e garante que nenhum cadastro seja salvo no banco de dados.
        invalid_data = self.cadastro_data.copy()
        invalid_data['CAD_NOME'] = '12345'

        url = reverse('processa_cadastro')
        request = self.factory.post(url, data=invalid_data)
        response = processa_cadastro(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cadastro/?status=4')
    def test_cadastro_render_template(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Cadastro.html')
    
    if __name__ == '__main__':
        import unittest
        unittest.main()