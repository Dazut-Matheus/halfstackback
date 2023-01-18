from rest_framework import serializers
from .models import Itens


class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = ("pedido", "empresa", "cliente", "produto", "quantidade")
