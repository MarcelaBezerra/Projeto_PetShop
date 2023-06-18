from django.test import TestCase
from .models import Agendamentos


class AgendamentosModelTest(TestCase):

#Esse código testa se o modelo Agendamentos está funcionando corretamente,
#  verificando se o atributo age_codigo é igual a 1. 
# Ele cria um objeto Agendamentos no banco de dados com age_codigo igual a 1 
# e depois recupera esse objeto para verificar se o valor do atributo está correto.
#  Se o teste passar, significa que o modelo está configurado corretamente.
#  Caso contrário, indica que há um problema com o modelo.

    def setUp(self):
        Agendamentos.objects.create(age_codigo=1)

    def test_agendamentos_model(self):
        agendamento = Agendamentos.objects.get(age_codigo=1)
        self.assertEqual(agendamento.age_codigo, 1)



  



