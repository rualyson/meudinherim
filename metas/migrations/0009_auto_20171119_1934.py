# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0008_auto_20171119_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metas',
            name='progresso',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
