# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 14:53
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0019_meta'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='attribute',
            managers=[
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='attributeentity',
            managers=[
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
