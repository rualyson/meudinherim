# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0003_auto_20171119_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamentosbanco',
            name='conta_a_pagar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contas_a_pagar.ContasAPagar'),
        ),
    ]
