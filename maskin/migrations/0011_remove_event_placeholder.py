# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-19 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maskin', '0010_event_placeholder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='placeholder',
        ),
    ]
