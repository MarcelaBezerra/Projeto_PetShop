from django.test import TestCase
from login.models import Login
from produtos.models import Produtos, Login_Produto


class ProdutosModelTestCase(TestCase):
    def setUp(self):
        self.login = Login.objects.create(log_codigo=1, log_email='test@example.com', log_senha='password')
        self.produto = Produtos.objects.create(pro_codigo=1, pro_valor=9.99, pro_nome='Produto 1', pro_tipo='Tipo 1', pro_qtde=10)
        self.login_produto = Login_Produto.objects.create(lp_codigo=1, log_codigo=self.login, pro_codigo=self.produto)
    # Verifica se a representação em string de um objeto Produtos está correta, 
    # para exibir informações sobre o produto.
    def test_produto_str(self):
        self.assertEqual(str(self.produto), 'Produto 1')

    # Verifica se os relacionamentos entre as models Login_Produto, 
    # Login e Produtos estão funcionando corretamente.
    def test_login_produto_relationships(self):
        self.assertEqual(self.login_produto.log_codigo, self.login)
        self.assertEqual(self.login_produto.pro_codigo, self.produto)
        self.assertEqual(self.login_produto.log_codigo.log_email, 'test@example.com')
        
    # Verifica se os atributos do objeto Produtos foram configurados corretamente.
    def test_produto_attributes(self):
        self.assertEqual(self.produto.pro_valor, 9.99)
        self.assertEqual(self.produto.pro_nome, 'Produto 1')
        self.assertEqual(self.produto.pro_tipo, 'Tipo 1')
        self.assertEqual(self.produto.pro_qtde, 10)
