# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-22 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advent_calendar', '0004_adventcalenderday_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adventcalenderday',
            options={'verbose_name': 'Advent calendar day', 'verbose_name_plural': 'Advent calendar days'},
        ),
    ]
