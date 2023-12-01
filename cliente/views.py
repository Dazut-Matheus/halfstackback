import datetime
import json
import random
import pytz
import requests
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import refresh_jwt_token
from cliente.models import PasswordResets
from cliente.models import Cliente, Tokens
from cliente.serializer import ClienteSerializer, TokensSerializer
from django.contrib.auth import logout, login
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class ViewLogin:
    # Função para recuperação de senha
    @csrf_exempt
    def forgotten(request):
        # Checagem do método utilizado no request
        if request.method == "POST":
            # Atribuição do body ao dicionário data
            data = json.loads(request.body)
            email = data["email"]
        else:
            return JsonResponse(
                {"success": False, "message": "Método inválido!"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        # Filtragem dos usuários de acordo com o email recebido no body
        person = Cliente.objects.filter(email=email).first()
        # Checagem se o usuário existe
        if person:
            # Geração de código de recuperação
            hash = str(random.random())[5:11]
            # Filtragem de acordo com o pedido de troca de senhas já ocorridas
            instance = PasswordResets.objects.filter(email=email)
            print(instance)
            if instance:
                # Deletar pedidos de troca antigos
                instance.delete()
            # Criação de email para envio do hash
            created_at = datetime.datetime.now()
            text_body = "Seu código de recuperação é: " + hash
            msg = EmailMultiAlternatives(
                subject="Recuperação de senha",
                from_email="alerta@ivare.com.br",
                to=[email],
                body=text_body,
            )
            # msg.send()

            # https://docs.djangoproject.com/en/4.1/topics/email/
            json_ = {"token": hash, "created_at": created_at, "email": email}
            # Salvando o pedido de recuperação de senha no PasswordResets
            S = PasswordResets(**json_)
            S.save()
            return JsonResponse(
                {"success": True, "message": "E-mail enviado com sucesso!"},
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"success": False, "message": "Usuario não encontrado"},
                status=status.HTTP_404_NOT_FOUND,
            )

    # Função para resetar a senha
    @csrf_exempt
    def reset_password(request):
        # Checagem do método request. Atribuição do body a variáveis utilizadas
        if request.method == "POST":
            data = json.loads(request.body)
            email = data["email"]
            token = data["token"]
            password = data["password"]
            password_confirmation = data["password_confirmation"]
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        # Filtragem do pedido para recuperação de senha de acordo com o email
        reset_person = PasswordResets.objects.filter(email=email).first()
        if reset_person:
            # Checagem se o token enviado pelo usuário corresponde ao gerado pelo sistema
            if reset_person.token == token:
                # Checagem se o token ainda é válido de acordo com tempo de expiração
                agora = datetime.datetime.now(tz=pytz.utc)
                expired = agora >= reset_person.created_at + datetime.timedelta(hours=8)

                if expired:
                    return JsonResponse(
                        {"success": False, "message": "Token expirado!"},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )
                else:
                    # Checagem se a senha e sua confirmação correspondem
                    if password == password_confirmation:
                        # Filtragem do usuário de acordo com o email
                        instance = Cliente.objects.filter(email=email).first()
                        # Checando se o usuário existe
                        if instance:
                            # Codificação da nova senha e atribuição ao usuário
                            instance.password = make_password(
                                password=data["password"],
                                salt=None,
                                hasher="pbkdf2_sha256",
                            )
                            # Salvando novos dados do usuário
                            instance.save()
                            # Deletando instância do pedido de mudança de senha do PasswordResets
                            reset_person.delete()
                            return JsonResponse(
                                {
                                    "success": True,
                                    "message": "senha trocada com sucesso!",
                                },
                                status=status.HTTP_200_OK,
                            )
                        else:
                            return JsonResponse(
                                {"success": False, "message": "Usuário não existe"},
                                status=status.HTTP_404_NOT_FOUND,
                            )
                    else:
                        return JsonResponse(
                            {"success": False, "message": "As senhas não coincidem"},
                            status=status.HTTP_428_PRECONDITION_REQUIRED,
                        )
            else:
                response = {
                    "success": False,
                    "message": "Verifique se as informações foram inseridas corretamente",
                    "data": {"errors": {"token": ["The selected token is invalid."]}},
                }

                return JsonResponse(
                    response, status=status.HTTP_422_UNPROCESSABLE_ENTITY
                )
        return JsonResponse(
            {"success": False, "message": "Usuario não encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )

    # Função para atualização de token de acesso
    @csrf_exempt
    def refresh(request):
        # Checagem do método da requisição
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                print(data.keys())
                if not "token" in data.keys():
                    return JsonResponse(
                        {"message": "Falta de token"},
                        status=status.HTTP_412_PRECONDITION_FAILED,
                    )
                print("AAAAAAAAAAAAAAAa")
            except Exception as e:
                print(e)
            # Formação do header e requisição da api de formação do novo token apartir do refresh
            headers = {"Content-type": "application/json", "Accept": "application/json"}
            requisicao = requests.post(
                "http://127.0.0.1:5000/api-token-refresh/",
                json={"token": data["token"]},
                headers=headers,
            )
            response = {
                "success": True,
                "message": "Tokens atualizados com sucesso",
                "data": {
                    "tokens": {
                        "access_token": requisicao.json()["token"],
                        "refresh_token": data["token"],
                    }
                },
            }
            return JsonResponse(response, status=status.HTTP_200_OK)
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    # Função de cadastro de novo usuário
    # @api_view(http_method_names=["POST"])
    @csrf_exempt
    def register(request):
        # Checagem do método da requisição
        if request.method == "POST":
            data = json.loads(request.body)
            if (
                data["nome"] == None
                or data["email"] == None
                or data["password"] == None
                or data["data_de_nascimento"] == None
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
            data["email_verified_at"] = False
            # Formação da senha encriptada
            data["password"] = make_password(
                password=data["password"], salt=None, hasher="pbkdf2_sha256"
            )
            # Serialização dos dados obtidos do body
            usuario_serializer = ClienteSerializer(
                data=data, context={"request": request}
            )

            # Caso as informações sejam válidas, o usuário será salvo/cadastrado
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return JsonResponse(
                    {"message": "Cliente Cadastrado"}, status=status.HTTP_201_CREATED
                )

            else:
                return JsonResponse(
                    usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse(
                {"message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    # Função de login
    @csrf_exempt
    def login_user(request):
        # Checagem do método da requisição
        if request.method == "POST":
            data = json.loads(request.body)
            email = data["email"]
            password = data["password"]

            # Filtragem do usuário de acordo com o email enviado no body
            instance = Cliente.objects.filter(email=email).first()
            # Checagem se o usuário se encontra no banco de dados
            if instance:
                # Checagem se a senha inserida corresponde com a salva
                che = check_password(password=password, encoded=instance.password)
                if che:
                    # Formação do token
                    payload = jwt_payload_handler(instance)
                    token = jwt_encode_handler(payload)

                    data_token = {}
                    data_token["cliente"] = instance.id
                    data_token["token"] = token
                    data_token["flag"] = True

                    tokens_serializer = TokensSerializer(
                        data=data_token, context={"request": request}
                    )
                    # Caso as informações sejam válidas, o usuário será salvo/cadastrado
                    instance_token = Tokens.objects.filter(cliente=instance.id)
                    if tokens_serializer.is_valid():
                        if instance_token:
                            instance_token.delete()
                        tokens_serializer.save()
                    else:
                        return JsonResponse(
                            tokens_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )

                    response = {
                        "success": True,
                        "message": "Sucesso ao realizar a autenticação.",
                        "data": {
                            "user": {
                                "id": instance.id,
                                "name": instance.nome,
                                "email": instance.email,
                                "email_verified_at": instance.email_verified_at,
                            },
                            "token": token,
                        },
                    }
                    # login(request, instance)
                    return JsonResponse(response, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(
                        {"sucess": False, "message": "Credenciais inválidas"},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )
            else:
                return JsonResponse(
                    {"sucess": False, "message": "Usuário não encontrado"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return JsonResponse(
                {"sucess": False, "message": "Método enviado não é um post"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    @api_view(http_method_names=["DELETE"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def del_user(request):
        if request.method == "DELETE":
            cliente = Cliente.objects.filter(id=request.user.id).first()
            if cliente:
                cliente.delete()
            else:
                return JsonResponse(
                    {"success": False, "message": "Cliete não encontrado"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return JsonResponse(
                {"success": True, "message": "Cliete excluído"},
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
    def get_users(request):
        if request.method == "GET":
            clientes = Cliente.objects.all()
            list_ = []
            for cliente in clientes:
                dict_ = {
                    "id": cliente.id,
                    "nome": cliente.nome,
                    "data_de_nascimento": cliente.data_de_nascimento,
                    "email": cliente.email,
                    "email_verified_at": cliente.email_verified_at,
                    "cidade": cliente.cidade,
                    "rua": cliente.rua,
                    "bairro": cliente.bairro,
                    "numero": cliente.numero,
                    "complemento": cliente.complemento,
                }
                list_.append(dict_)
            return JsonResponse(
                {"success": True, "message": list_},
                status=status.HTTP_200_OK,
            )
        else:
            return JsonResponse(
                {"success": False, "message": "Método enviado não é um GET"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    @api_view(http_method_names=["PUT"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def put_user_id(request, id):
        # Checagem do método da requisição
        cliente = Cliente.objects.filter(id=id).first()
        if not cliente:
            return JsonResponse(
                {
                    "success": False,
                    "message": "Cliente não encontrado",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        if request.method == "PUT":
            try:
                data = json.loads(request.body)
                if (
                    data["nome"] == None
                    or data["email"] == None
                    or data["password"] == None
                    or data["data_de_nascimento"] == None
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

            cliente.nome = data["nome"]
            cliente.email = data["email"]
            cliente.password = make_password(
                password=data["password"], salt=None, hasher="pbkdf2_sha256"
            )
            cliente.data_de_nascimento = data["data_de_nascimento"]
            cliente.cidade = data["cidade"]
            cliente.rua = data["rua"]
            cliente.bairro = data["bairro"]
            cliente.numero = data["numero"]
            cliente.empresa = data["empresa"]
            cliente.save()
            return JsonResponse(
                {"message": "Cliente Atualizado!"}, status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                {"message": "Método enviado não é um put"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
