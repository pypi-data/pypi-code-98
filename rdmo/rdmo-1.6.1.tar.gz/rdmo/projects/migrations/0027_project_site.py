# Generated by Django 2.2.2 on 2019-06-17 11:49

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('projects', '0026_django2'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='project',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='site',
            field=models.ForeignKey(default=1, help_text='The site this view belongs to (in a multi site setup).', on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='Site'),
            preserve_default=False,
        ),
    ]
