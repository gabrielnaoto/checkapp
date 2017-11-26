# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 12:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20171125_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='recebido',
            name='repassado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='banco',
            name='data_cadastro',
            field=models.DateField(default=datetime.datetime(2017, 11, 26, 12, 58, 3, 703050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateField(default=datetime.datetime(2017, 11, 26, 12, 58, 3, 703050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='emitido',
            name='data_cadastro',
            field=models.DateField(default=datetime.datetime(2017, 11, 26, 12, 58, 3, 703050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='data_cadastro',
            field=models.DateField(default=datetime.datetime(2017, 11, 26, 12, 58, 3, 703050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recebido',
            name='data_cadastro',
            field=models.DateField(default=datetime.datetime(2017, 11, 26, 12, 58, 3, 703050, tzinfo=utc)),
        ),
    ]
