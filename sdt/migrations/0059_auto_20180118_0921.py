# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdt', '0058_ucs_developer_balance_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucs_operator',
            name='operator_id',
            field=models.IntegerField(null=True),
        ),
    ]
