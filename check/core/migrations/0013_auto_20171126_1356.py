# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20171126_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='emitido',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='recebido',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
