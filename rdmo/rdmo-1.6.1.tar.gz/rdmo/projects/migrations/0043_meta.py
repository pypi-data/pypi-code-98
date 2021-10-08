# Generated by Django 2.2.16 on 2020-10-28 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0042_allow_site_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='catalog',
            field=models.ForeignKey(help_text='The catalog which will be used for this project.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='questions.Catalog', verbose_name='Catalog'),
        ),
    ]
