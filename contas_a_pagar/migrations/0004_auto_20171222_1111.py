# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas_a_pagar', '0003_auto_20171221_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contasapagar',
            name='descricao',
            field=models.CharField(max_length=64),
        ),
    ]
