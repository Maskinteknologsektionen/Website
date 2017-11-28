# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-19 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advent_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adventcalendarconfig',
            options={'verbose_name': 'Advent calendar', 'verbose_name_plural': 'Advent calendars'},
        ),
        migrations.AddField(
            model_name='adventcalendarconfig',
            name='background',
            field=models.ImageField(default=None, upload_to=b'', verbose_name='background image'),
        ),
        migrations.AlterUniqueTogether(
            name='adventcalendarconfig',
            unique_together=set([]),
        ),
    ]