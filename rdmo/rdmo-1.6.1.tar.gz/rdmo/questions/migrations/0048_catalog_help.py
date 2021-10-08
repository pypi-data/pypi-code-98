# Generated by Django 2.2.7 on 2019-11-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0047_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='help_lang1',
            field=models.TextField(blank=True, help_text='The help text for this catalog in the primary language.', verbose_name='Help (primary)'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='help_lang2',
            field=models.TextField(blank=True, help_text='The help text for this catalog in the secondary language.', verbose_name='Help (secondary)'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='help_lang3',
            field=models.TextField(blank=True, help_text='The help text for this catalog in the tertiary language.', verbose_name='Help (tertiary)'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='help_lang4',
            field=models.TextField(blank=True, help_text='The help text for this catalog in the quaternary language.', verbose_name='Help (quaternary)'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='help_lang5',
            field=models.TextField(blank=True, help_text='The help text for this catalog in the quinary language.', verbose_name='Help (quinary)'),
        ),
    ]
