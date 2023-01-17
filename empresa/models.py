from django.db import models
from produto.models import Produto
# Create your models here.
class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=48)
    cnpj = models.CharField(max_length=48)
    telefone = models.CharField(max_length=48)
    foto = models.CharField(max_length=48, null=True, blank=True)
    produtos = models.ManyToManyField(Produto)
    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = "empresa"