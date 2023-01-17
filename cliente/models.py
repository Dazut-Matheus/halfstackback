from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class Cliente(AbstractBaseUser):
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
    
    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = "cliente"