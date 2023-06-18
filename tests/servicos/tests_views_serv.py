from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .views import servicos

class ServicosViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_servicos_view_with_unauthenticated_user(self):
        # Cria uma requisição GET para a view sem usuário autenticado
        response = self.client.get(reverse('servicos'))
        
        # Verifica se a resposta é um redirecionamento para a página de login com o status correto
        self.assertRedirects(response, '/login/?status=2')
    