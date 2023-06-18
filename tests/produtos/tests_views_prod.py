from django.test import TestCase, Client
from django.urls import reverse
from .views import produtos, categorias, compra

class ProdutosViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_produtos = reverse('produtos')
        self.url_categorias = reverse('categorias')
        self.url_compra = reverse('compra')

    def test_produtos_view_without_authenticated_user(self):
        # Verifica se um usuário não autenticado é redirecionado para
        # a página de login ao tentar acessar a visualização de produtos.
        self.client.session.clear()
        response = self.client.get(self.url_produtos)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?status=2')

    def test_categorias_view_without_authenticated_user(self):
        # Verifica se um usuário não autenticado é redirecionado para 
        # a página de login ao tentar acessar a visualização de categorias.
        self.client.session.clear()
        response = self.client.get(self.url_categorias)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?status=2')

    def test_compra_view_without_authenticated_user(self):
        # Verifica se um usuário não autenticado é redirecionado para 
        # a página de login ao tentar acessar a visualização de compra.
        self.client.session.clear()
        response = self.client.get(self.url_compra)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?status=2')
    
    