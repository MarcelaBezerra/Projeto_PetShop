from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, time
from servicos.models import Banhoetosa, Consultas, Adestramento
from .models import Agendamentos

class AgendamentosViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.agendamentos_url = reverse('agendamentos')
    # Verifica se usuários não autenticados têm acesso negado à
    # visualização de agendamentos e são redirecionados corretamente ou recebem uma mensagem de erro apropriada.
    def test_agendamentos_view_without_authenticated_user(self):
        response = self.client.get(self.agendamentos_url)
        self.assertEqual(response.status_code, 302)  # Redirecionamento esperado
        self.assertRedirects(response, '/login/?status=2')
    