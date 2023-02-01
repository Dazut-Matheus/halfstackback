"""halfstack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token
from cliente.views import ViewLogin
from empresa.views import ViewEmpresa
from produto.views import ViewProduto
from pedido.views import ViewPedido
from itens.views import ViewItens

urlpatterns = [
    path("login/", ViewLogin.login_user),
    path("forgotten/", ViewLogin.forgotten),
    path("delete_user/", ViewLogin.del_user),
    path("reset_password/", ViewLogin.reset_password),
    path("api-token-refresh/", refresh_jwt_token),
    path("refresh/", ViewLogin.refresh),
    path("register_users/", ViewLogin.register),
    path("register_empresa/", ViewEmpresa.register),
    path("register_produto/", ViewProduto.register),
    path("register_pedido/", ViewPedido.register),
    path("register_itens/", ViewItens.register),
    path("get_pedido/<int:id>/show", ViewPedido.get_pedido_id),
    path("get_produto_empresa/<int:id>/show", ViewProduto.get_produto_empresa),
]
