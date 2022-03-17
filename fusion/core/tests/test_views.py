from urllib import request
from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': "felicity@gmail.com",
            'assunto': 'meu assunto',
            'mensagem': 'minha mensagem qualquer'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data = self.dados)
        self.assertEquals(request.status_code, 302) # Em http o redirect é representado pelo código 302. Nossa view faz um redirect quando tem sucesso em fazer o post.

    def test_form_invalid(self):
        dados = {
            'nome': 'Felicity Jones',
            'assunto': 'um assunto'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)