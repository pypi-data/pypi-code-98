# Generated by Django 1.9.8 on 2016-08-01 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20160728_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditem',
            name='is_main',
            field=models.BooleanField(default=True, verbose_name='Is Main'),
        ),
    ]
