# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-19 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advent_calendar', '0003_auto_20171119_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='adventcalenderday',
            name='order',
            field=models.IntegerField(default=0, verbose_name='display order'),
        ),
    ]
