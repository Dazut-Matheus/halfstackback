from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from produto.models import Produto
from produto.serializer import ProdutoSerializer

# Create your views here.
class ViewProduto:
    @csrf_exempt
    def register(request):
        # Checagem do método da requisição
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                if (
                    data["empresa"] == None
                    or data["nome"] == None
                    or data["descricao"] == None
                    or data["valor"] == None
                ):
                    return JsonResponse(
                        {
                            "success": False,
                            "message": "Falta de preenchimento de campo obrigatório",
                        },
                        status=status.HTTP_412_PRECONDITION_FAILED,
                    )
            except Exception as e:
                print(e)
            # Serialização dos dados obtidos do body
            produto_serilizer = ProdutoSerializer(
                data=data, context={"request": request}
            )

            # Caso as informações sejam válidas, o usuário será salvo/cadastrado
            if produto_serilizer.is_valid():
                produto_serilizer.save()
                return JsonResponse(
                    {"message": "Produto Cadastrado"}, status=status.HTTP_201_CREATED
                )

            else:
                return JsonResponse(
                    produto_serilizer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
