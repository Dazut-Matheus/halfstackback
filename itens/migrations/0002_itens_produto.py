# Generated by Django 3.2.16 on 2023-01-18 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produto_empresa'),
        ('itens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itens',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='produto.produto'),
            preserve_default=False,
        ),
    ]
