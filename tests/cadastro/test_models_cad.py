from django.test import TestCase
from .models import Cadastro

class CadastroModelTestCase(TestCase):
    def setUp(self):
        self.cadastro = Cadastro.objects.create(
            cad_nome='John Doe',
            cad_email='johndoe@example.com',
            cad_rua='Street',
            cad_numero='123',
            cad_bairro='Neighborhood',
            cad_cidade='City',
            cad_contato='1234567890',
            cad_senha='password'
        )
    
    def test_cadastro_model(self):
        self.assertEqual(str(self.cadastro), 'John Doe')
        self.assertEqual(self.cadastro.cad_nome, 'John Doe')
        self.assertEqual(self.cadastro.cad_email, 'johndoe@example.com')
        self.assertEqual(self.cadastro.cad_rua, 'Street')
        self.assertEqual(self.cadastro.cad_numero, '123')
        self.assertEqual(self.cadastro.cad_bairro, 'Neighborhood')
        self.assertEqual(self.cadastro.cad_cidade, 'City')
        self.assertEqual(self.cadastro.cad_contato, '1234567890')
        self.assertEqual(self.cadastro.cad_senha, 'password')
