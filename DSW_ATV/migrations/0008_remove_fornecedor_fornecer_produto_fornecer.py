# Generated by Django 5.1.4 on 2024-12-13 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSW_ATV', '0007_fornecedor_fornecer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='fornecer',
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DSW_ATV.fornecedor'),
            preserve_default=False,
        ),
    ]
