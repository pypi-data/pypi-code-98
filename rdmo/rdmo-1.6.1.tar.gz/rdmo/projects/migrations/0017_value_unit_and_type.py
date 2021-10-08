# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-04 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_catalog_on_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='unit',
            field=models.CharField(blank=True, help_text='Unit for this value.', max_length=64, verbose_name='Unit', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='value',
            name='value_type',
            field=models.CharField(choices=[(b'text', 'Text'), (b'url', 'URL'), (b'integer', 'Integer'), (b'float', 'Float'), (b'boolean', 'Boolean'), (b'datetime', 'Datetime'), (b'options', 'Options')], default='text', help_text='Type of this value.', max_length=8, verbose_name='Value type'),
            preserve_default=False,
        ),
    ]
