# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-21 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_move_attribute_to_attributeentity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeframe',
            name='end_attribute',
            field=models.ForeignKey(blank=True, help_text='The attribute that is setting the end date for this task (optional, if no end date attribute is given, the start date attribute sets also the end date).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='domain.Attribute', verbose_name='End date attribute'),
        ),
        migrations.AlterField(
            model_name='timeframe',
            name='start_attribute',
            field=models.ForeignKey(blank=True, help_text='The attribute that is setting the start date for this task.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='domain.Attribute', verbose_name='Start date attribute'),
        ),
    ]
