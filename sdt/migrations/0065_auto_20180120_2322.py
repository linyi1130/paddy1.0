# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sdt', '0064_auto_20180120_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucs_result_table',
            name='active_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
