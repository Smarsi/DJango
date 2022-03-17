import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class GetFilePathTestCase(TestCase):

    #Para cada unidade crie um TestCase

    '''
    Vamos criar uma função de setUp que criará um arquivo com o uuid e iremos colocar uma extensão nele.
    Basicamente nossa função de testes irá comparar o tamanho do nome do arquivo criado com o tamanho do nome do arquivo subido no sistema.
    Estamos tentando nos certificar que os arquivos estão sendo nomeados corretamente e que nenhum erro está ocorrendo no processo.
    O tamanho do nome deve ser sempre = 40.
    '''

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServicoTestCase(TestCase):
    
    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):

    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)

class FeaturesTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make('Features')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.feature)