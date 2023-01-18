import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from pedido.serializer import PedidoSerializer
from pedido.models import Pedido
from itens.models import Itens
from empresa.models import Empresa

# Create your views here.


class ViewPedido:
    @csrf_exempt
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
                    or data["empresa"] == None
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

            # Caso as informações sejam válidas, o usuário será salvo/cadastrado
            if pedido_serilizer.is_valid():
                pedido_serilizer.save()
                return JsonResponse(
                    {"message": "Pedido Cadastrado"}, status=status.HTTP_201_CREATED
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

    @csrf_exempt
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
                    {"produto": item.produto.id, "quantidade": item.quantidade}
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
