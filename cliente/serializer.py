from rest_framework import serializers
from .models import Cliente, Tokens


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            "nome",
            "data_de_nascimento",
            "email",
            "email_verified_at",
            "password",
            "cidade",
            "rua",
            "bairro",
            "numero",
            "complemento",
            "empresa",
        )


class TokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = (
            "user",
            "flag",
            "token",
        )
