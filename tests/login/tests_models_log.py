from django.test import TestCase
from .models import Login

class LoginModelTestCase(TestCase):
    def setUp(self):
        self.login = Login.objects.create(log_email='test@example.com', log_senha='password')
# Verifica se a representação em string do objeto Login é igual ao email fornecido.
    def test_str_representation(self):
        self.assertEqual(str(self.login), 'test@example.com')
# Os métodos test_log_email_max_length e test_log_senha_max_length verificam se os campos log_email e log_senha têm o comprimento máximo definido como 25.
    def test_log_email_max_length(self):
        max_length = self.login._meta.get_field('log_email').max_length
        self.assertEqual(max_length, 25)

    def test_log_senha_max_length(self):
        max_length = self.login._meta.get_field('log_senha').max_length
        self.assertEqual(max_length, 25)
# Verifica se o campo log_codigo é definido como chave primária.
    def test_log_codigo_primary_key(self):
        is_primary_key = self.login._meta.get_field('log_codigo').primary_key
        self.assertTrue(is_primary_key)
# Verifica se o campo log_codigo não é editável.
    def test_log_codigo_not_editable(self):
        is_editable = self.login._meta.get_field('log_codigo').editable
        self.assertFalse(is_editable)
