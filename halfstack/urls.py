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
from django.contrib.auth import views as auth_views

urlpatterns = [
    # login
    path("login/", ViewLogin.login_user),
    path("forgotten/", ViewLogin.forgotten),
    path("reset_password/", ViewLogin.reset_password),
    path("api-token-refresh/", refresh_jwt_token),
    path("refresh/", ViewLogin.refresh),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # users
    path("delete_user/", ViewLogin.del_user),
    path("register_users/", ViewLogin.register),
    path("get_users/", ViewLogin.get_users),
    # Empresa
    path("register_empresa/", ViewEmpresa.register),
    path("get_empresas/", ViewEmpresa.get_empresas),
    # Produto
    path("register_produto/", ViewProduto.register),
    path("get_produto_empresa/<int:id>/show", ViewProduto.get_produto_empresa),
    # Pedido
    path("register_pedido/", ViewPedido.register),
    path("get_pedido/<int:id>/show", ViewPedido.get_pedido_id),
    # Itens
    path("register_itens/", ViewItens.register),
]
