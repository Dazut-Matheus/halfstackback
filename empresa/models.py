from django.db import models
# Create your models here.
class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=48)
    cnpj = models.CharField(max_length=48, null=True, blank=True, default="")
    telefone = models.CharField(max_length=48)
    cidade = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, null=True, blank=True, default="")
    def __str__(self):
        return str(self.nome)

    class Meta:
        db_table = "empresa"