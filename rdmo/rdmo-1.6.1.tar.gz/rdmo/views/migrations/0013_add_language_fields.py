# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-05 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0012_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='help_lang3',
            field=models.TextField(blank=True, help_text='The help text for this view in the tertiary language.', null=True, verbose_name='Help (tertiary)'),
        ),
        migrations.AddField(
            model_name='view',
            name='help_lang4',
            field=models.TextField(blank=True, help_text='The help text for this view in the quaternary language.', null=True, verbose_name='Help (quaternary)'),
        ),
        migrations.AddField(
            model_name='view',
            name='help_lang5',
            field=models.TextField(blank=True, help_text='The help text for this view in the quinary language.', null=True, verbose_name='Help (quinary)'),
        ),
        migrations.AddField(
            model_name='view',
            name='title_lang3',
            field=models.CharField(blank=True, help_text='The title for this view in the tertiary language.', max_length=256, null=True, verbose_name='Title (tertiary)'),
        ),
        migrations.AddField(
            model_name='view',
            name='title_lang4',
            field=models.CharField(blank=True, help_text='The title for this view in the quaternary language.', max_length=256, null=True, verbose_name='Title (quaternary)'),
        ),
        migrations.AddField(
            model_name='view',
            name='title_lang5',
            field=models.CharField(blank=True, help_text='The title for this view in the quinary language.', max_length=256, null=True, verbose_name='Title (quinary)'),
        ),
    ]
