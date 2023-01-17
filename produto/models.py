from django.db import models

# Create your models here.
class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=48)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    valor = models.FloatField()
    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = "produto"