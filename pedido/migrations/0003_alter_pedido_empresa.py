# Generated by Django 3.2.16 on 2023-02-01 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_remove_empresa_foto'),
        ('pedido', '0002_remove_pedido_cliente_endereco_pedido_bairro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]
