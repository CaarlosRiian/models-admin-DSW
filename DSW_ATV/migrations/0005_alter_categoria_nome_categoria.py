# Generated by Django 5.1.4 on 2024-12-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSW_ATV', '0004_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_categoria',
            field=models.CharField(max_length=255, verbose_name='Nome da Categoria'),
        ),
    ]