# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_auto_20170903_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='trace_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]