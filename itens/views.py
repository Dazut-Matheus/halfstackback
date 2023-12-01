import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from itens.serializer import ItensSerializer
from itens.models import Itens
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.


class ViewItens:
    @api_view(http_method_names=["POST"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def register(request):
        # Checagem do método da requisição
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                if (
                    data["pedido"] == None
                    or data["empresa"] == None
                    or data["cliente"] == None
                    or data["produto"] == None
                    or data["quantidade"] == None
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
            instance_itens = Itens.objects.filter(
                pedido=data["pedido"],
                empresa=data["empresa"],
                cliente=data["cliente"],
                produto=data["produto"],
            ).first()
            if instance_itens:
                instance_itens.quantidade = (
                    data["quantidade"] + instance_itens.quantidade
                )
                instance_itens.save()
                itens_serilizer = ItensSerializer(instance_itens)

                return JsonResponse(
                    {"message": "Item Adicionado", "data": itens_serilizer.data},
                    status=status.HTTP_201_CREATED,
                )
            # print(instance_itens)
            itens_serilizer = ItensSerializer(data=data, context={"request": request})

            # Caso as informações sejam válidas, o usuário será salvo/cadastrado
            if itens_serilizer.is_valid():
                itens_serilizer.save()
                return JsonResponse(
                    {"message": "Item Adicionado", "data": itens_serilizer.data},
                    status=status.HTTP_201_CREATED,
                )

            else:
                return JsonResponse(
                    itens_serilizer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    @api_view(http_method_names=["DELETE"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def del_item_id(request, id):
        if request.method == "DELETE":
            item = Itens.objects.filter(id=id).first()
            if item:
                item.delete()
            else:
                return JsonResponse(
                    {"success": False, "message": "item não encontrado"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return JsonResponse(
                {"success": True, "message": "item excluído"},
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"success": False, "message": "Método enviado não é um DELETE"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
