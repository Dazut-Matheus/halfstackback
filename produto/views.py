from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from produto.models import Produto
from produto.serializer import ProdutoSerializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from empresa.models import Empresa

# Create your views here.
class ViewProduto:
    @api_view(http_method_names=["POST"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
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

    @api_view(http_method_names=["DELETE"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def del_produto_id(request, id):
        if request.method == "DELETE":
            produto = Produto.objects.filter(id=id).first()
            if produto:
                produto.delete()
            else:
                return JsonResponse(
                    {"success": False, "message": "produto não encontrado"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return JsonResponse(
                {"success": True, "message": "produto excluído"},
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"success": False, "message": "Método enviado não é um DELETE"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    @api_view(http_method_names=["GET"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def get_produto_empresa(request, id):
        # Checagem do método da requisição
        if request.method == "GET":
            instance_empresa = Empresa.objects.filter(id=id).first()
            instance_produtos = Produto.objects.filter(empresa=instance_empresa.id)

            dict_prod = []
            for item in instance_produtos:
                dict_prod.append(
                    {
                        "id": item.id,
                        "produto": item.nome,
                        "descricao": item.descricao,
                        "valor": item.valor,
                    }
                )
            print(dict_prod)
            response = {
                "empresa": {
                    "nome": instance_empresa.nome,
                    "telefone": instance_empresa.telefone,
                },
                "Produtos": dict_prod,
            }
            return JsonResponse({"message": response}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    @api_view(http_method_names=["POST"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def busca_produto_preco(request):
        # Checagem do método da requisição
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                if not "max" in data.keys() or not "min" in data.keys():

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
            if not data["min"] == None and not data["max"] == None:
                # print(1)
                produtos = Produto.objects.filter(
                    valor__gte=data["min"], valor__lte=data["max"]
                )
            if not data["min"] == None and data["max"] == None:
                # print(2)
                produtos = Produto.objects.filter(valor__gte=data["min"])
            if data["min"] == None and not data["max"] == None:
                # print(3)
                produtos = Produto.objects.filter(valor__lte=data["max"])
            if data["min"] == None and data["max"] == None:
                # print(4)
                produtos = Produto.objects.all()

            dict_prod = []
            for item in produtos:
                dict_prod.append(
                    {
                        "id": item.id,
                        "empresa": item.empresa.nome,
                        "produto": item.nome,
                        "descricao": item.descricao,
                        "valor": item.valor,
                    }
                )
            # print(dict_prod)
            return JsonResponse(
                {
                    "success": False,
                    "message": dict_prod,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
