from django.db import models

#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsuarioManager(BaseUserManager):

    use_in_migrations = True #Estamos apontando que esse model será usado sim nos banco de dados (Irá virar tabela)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_field.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user()

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15, default='')
    if_staff = models.BooleanField('Membro de equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone'] # O E-mail e senha por serem utilizados para login serão OBRIGATÓRIOS por padrão pelo DJango.

    def __str__(self):
        return self.email

    objects = UsuarioManager() #Temos que adicionar essa configuração para dizer ao DJango que o UserManager utilizado deve ser esse. Se não definirmos isso o DJango usará o UserManager padrão do sistema (e consequentimente a autenticação por e-mail não irá funcionar).