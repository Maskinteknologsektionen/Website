# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-27 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maskin', '0003_auto_20170917_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='start_year',
            field=models.IntegerField(default=0, verbose_name='Start year'),
        ),
    ]