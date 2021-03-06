# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdt', '0074_menu_tree_l1_menu_tree_l2_permission_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_tree_l1',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='menu_tree_l1',
            name='tree_desc',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='menu_tree_l1',
            name='url',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='menu_tree_l2',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='menu_tree_l2',
            name='tree_desc',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='menu_tree_l2',
            name='url',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='permission_menu',
            name='tree_l1_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='permission_menu',
            name='tree_l2_id',
            field=models.IntegerField(null=True),
        ),
    ]
