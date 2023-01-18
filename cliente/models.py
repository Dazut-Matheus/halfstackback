from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from empresa.models import Empresa
# Create your models here.
class Cliente(AbstractBaseUser):
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    
    username = None
    last_login = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    data_de_nascimento = models.DateField()
    email = models.EmailField(unique=True, max_length=255)
    email_verified_at = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    cidade = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = "cliente"
class PasswordResets(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        db_table = "password_resets"
class Tokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    token = models.CharField(max_length=500)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "auth_tokens"