# Generated by Django 5.1.4 on 2025-01-30 18:38

import DSW_ATV.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSW_ATV', '0005_alter_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='qntd_estoque',
            field=models.IntegerField(validators=[DSW_ATV.validators.validate_stock]),
        ),
    ]
