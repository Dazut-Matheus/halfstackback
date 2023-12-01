import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from pedido.serializer import PedidoSerializer
from pedido.models import Pedido
from itens.models import Itens
from empresa.models import Empresa
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.


class ViewPedido:
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
                    or data["cliente_nome"] == None
                    or data["cidade"] == None
                    or data["rua"] == None
                    or data["bairro"] == None
                    or data["numero"] == None
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
            pedido_serilizer = PedidoSerializer(data=data, context={"request": request})
            # print(pedido_serilizer)
            # print(pedido_serilizer.data)
            # Caso as informações sejam válidas, o usuário será salvo/cadastrado
            if pedido_serilizer.is_valid():
                pedido_serilizer.save()
                return JsonResponse(
                    {"message": "Pedido Cadastrado", "data": pedido_serilizer.data},
                    status=status.HTTP_201_CREATED,
                )

            else:
                return JsonResponse(
                    pedido_serilizer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    @api_view(http_method_names=["GET"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def get_pedido_id(request, id):
        # Checagem do método da requisição
        if request.method == "GET":
            instance_pedido = Pedido.objects.filter(id=id).first()
            instance_itens = Itens.objects.filter(pedido=id)
            instance_empresa = Empresa.objects.filter(
                id=instance_pedido.empresa.id
            ).first()
            dict_item = []
            for item in instance_itens:
                dict_item.append(
                    {"produto": item.produto.nome, "quantidade": item.quantidade}
                )
            print(dict_item)
            response = {
                "pedido": id,
                "empresa": {
                    "nome": instance_empresa.nome,
                    "telefone": instance_empresa.telefone,
                },
                "cliente_nome": instance_pedido.cliente_nome,
                "endereco": {
                    "cidade": instance_pedido.cidade,
                    "rua": instance_pedido.rua,
                    "bairro": instance_pedido.bairro,
                    "numero": instance_pedido.numero,
                },
                "itens": dict_item,
            }
            return JsonResponse({"message": response}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    @api_view(http_method_names=["DELETE"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def del_pedido_id(request, id):
        if request.method == "DELETE":
            pedido = Pedido.objects.filter(id=id).first()
            if pedido:
                pedido.delete()
            else:
                return JsonResponse(
                    {"success": False, "message": "pedido não encontrado"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return JsonResponse(
                {"success": True, "message": "pedido excluído"},
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"success": False, "message": "Método enviado não é um DELETE"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
