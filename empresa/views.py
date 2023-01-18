from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import JsonResponse
from empresa.serializer import EmpresaSerializer
from empresa.models import Empresa

# Create your views here.


class ViewEmpresa:
    @csrf_exempt
    def register(request):
        # Checagem do método da requisição
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                if (
                    data["nome"] == None
                    or data["cnpj"] == None
                    or data["telefone"] == None
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
            empresa_serilizer = EmpresaSerializer(
                data=data, context={"request": request}
            )

            # Caso as informações sejam válidas, o usuário será salvo/cadastrado
            if empresa_serilizer.is_valid():
                empresa_serilizer.save()
                return JsonResponse(
                    {"message": "Empresa Cadastrada"}, status=status.HTTP_201_CREATED
                )

            else:
                return JsonResponse(
                    empresa_serilizer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
