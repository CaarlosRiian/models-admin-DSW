# Generated by Django 5.1.4 on 2025-01-26 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DSW_ATV', '0003_categoria_fornecedor_produto_categorias_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='fornecer',
            new_name='fornecedor',
        ),
    ]
