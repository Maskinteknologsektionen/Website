# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-09 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('maskin', '0012_newsbloglatestarticlebycategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='maskin_memberpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('ShowForMembers', models.BooleanField(choices=[(True, 'Show for members only.'), (False, 'Show for none members only.')], default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
