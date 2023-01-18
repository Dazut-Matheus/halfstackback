from django.db import models
from empresa.models import Empresa

# Create your models here.
class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nome = models.CharField(max_length=48)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    valor = models.FloatField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "produto"
