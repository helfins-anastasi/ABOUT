# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-03 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170703_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restriction',
            name='cvalue',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restriction',
            name='ivalue',
            field=models.IntegerField(null=True),
        ),
    ]
