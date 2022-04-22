from django.db import models
from django.contrib.auth import get_user_model

# Temos 3 formas de usar o Django User Model

'''
A terceira forma é a que usaremos nesse projeto.
Basicamente chamando essa função (get_user_model) iremos pedir para o DJango trazer o user model correto. Ou seja,
se tivermos modificado o UserModel através do settings o DJango pegará este, caso contrário ele chamará o padrão.

'''

# Terceira forma de usar o DJango User Model (Chamando a função get_user_model)
class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name = 'Autor', on_delete = models.CASCADE)
    titulo = models.CharField('Títutlo', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo


'''
# Primeira forma de usar o DJango User Model (Chamando o módulo padrão do DJango)

from django.contrib.auth.models import User

class Post(models.Model):
    autor = models.ForeignKey(User, verbose_name = 'Autor', on_delete = models.CASCADE)
    titulo = models.CharField('Títutlo', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo


#Segunda forma de usar o django user model (Definindo um UserModel costumizado)

from django.conf import settings

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'Autor', on_delete = models.CASCADE)
    titulo = models.CharField('Títutlo', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo

'''