# Generated by Django 4.1.5 on 2023-01-18 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0003_remove_empresa_foto"),
        ("produto", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="empresa",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="empresa.empresa",
            ),
            preserve_default=False,
        ),
    ]