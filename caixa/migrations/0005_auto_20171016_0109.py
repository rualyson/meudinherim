# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 03:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0004_auto_20171016_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamentoscaixa',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
