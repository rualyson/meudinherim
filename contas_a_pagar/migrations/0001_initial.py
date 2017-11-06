# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 01:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caixa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContasAPagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('descricao', models.CharField(max_length=32)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('paga', models.BooleanField()),
                ('categoria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='caixa.Categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
