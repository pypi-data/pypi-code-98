# Generated by Django 1.9.7 on 2016-07-29 03:45
from __future__ import unicode_literals

from django.db import migrations


def update_runtime_config(apps, schema):
    Module = apps.get_model('modules', 'Module')
    models_mapping = {
        'shop-manufactures': 'shop.ProductManufacturer',
        'shop-labels': 'shop.ProductLabel',
    }
    for module in ('shop-manufactures', 'shop-labels'):
        try:
            m = Module.objects.get(slug=module)
        except Module.DoesNotExist:
            continue

        m.slug = 'dict-%s' % m.slug
        m.config = {
            "model": models_mapping.get(module)
        }
        m.save()


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0006_insert_order_statuses'),
    ]

    operations = [
        migrations.RunPython(update_runtime_config)
    ]
