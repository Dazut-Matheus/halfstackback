from django.db import models
from empresa.models import Empresa
from pedido.models import Pedido
from cliente.models import Cliente
# Create your models here.
class Itens(models.Model):
    id = models.BigAutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "itens"