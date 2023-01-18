from django.db import models
from empresa.models import Empresa
# Create your models here.
class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    cliente_nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "pedido"