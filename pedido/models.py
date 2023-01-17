from django.db import models
from empresa.models import Empresa
# Create your models here.
class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    itens = models.CharField(max_length=48)
    fl_super_admin = models.IntegerField()
    fl_alert = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "pedido"