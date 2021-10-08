# Generated by Django 2.2.18 on 2021-03-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0056_question_is_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='default_text_lang1',
            field=models.TextField(blank=True, help_text='The default text value for this question in the primary language.', null=True, verbose_name='Default text value (primary)'),
        ),
        migrations.AddField(
            model_name='question',
            name='default_text_lang2',
            field=models.TextField(blank=True, help_text='The default text value for this question in the secondary language.', null=True, verbose_name='Default text value (secondary)'),
        ),
        migrations.AddField(
            model_name='question',
            name='default_text_lang3',
            field=models.TextField(blank=True, help_text='The default text value for this question in the tertiary language.', null=True, verbose_name='Default text value (tertiary)'),
        ),
        migrations.AddField(
            model_name='question',
            name='default_text_lang4',
            field=models.TextField(blank=True, help_text='The default text value for this question in the quaternary language.', null=True, verbose_name='Default text value (quaternary)'),
        ),
        migrations.AddField(
            model_name='question',
            name='default_text_lang5',
            field=models.TextField(blank=True, help_text='The default text value for this question in the quinary language.', null=True, verbose_name='Default text value (quinary)'),
        ),
    ]
