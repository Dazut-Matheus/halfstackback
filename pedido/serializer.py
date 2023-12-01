from rest_framework import serializers
from .models import Pedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = (
            "id",
            "empresa",
            "cliente_nome",
            "cidade",
            "rua",
            "bairro",
            "numero",
            "complemento",
        )
