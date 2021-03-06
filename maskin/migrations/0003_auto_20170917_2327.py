# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-17 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maskin', '0002_auto_20170917_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='member',
            field=models.ManyToManyField(blank=True, to='maskin.SchoolYear', verbose_name='Member years'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='program',
            field=models.CharField(blank=True, choices=[(b'M', 'Mechanical engingering'), (b'DPU', 'Design and Product Development'), (b'EMM', 'Energy-Environment-Management'), (b'MASTER', 'Masterprogram'), (b'OTHER', 'Other')], max_length=10, verbose_name='Program'),
        ),
    ]
