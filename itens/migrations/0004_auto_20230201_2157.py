# Generated by Django 3.2.16 on 2023-02-01 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_remove_pedido_cliente_endereco_pedido_bairro_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produto', '0002_produto_empresa'),
        ('empresa', '0003_remove_empresa_foto'),
        ('itens', '0003_itens_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itens',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='itens',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
        migrations.AlterField(
            model_name='itens',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido'),
        ),
        migrations.AlterField(
            model_name='itens',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto'),
        ),
    ]