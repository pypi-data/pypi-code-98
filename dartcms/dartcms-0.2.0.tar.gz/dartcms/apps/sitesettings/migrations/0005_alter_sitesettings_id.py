# Generated by Django 3.2.8 on 2021-10-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0004_auto_20180130_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
