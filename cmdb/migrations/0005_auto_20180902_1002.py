# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_auto_20180902_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serverinfo',
            options={},
        ),
        migrations.RemoveField(
            model_name='serverinfo',
            name='created',
        ),
    ]