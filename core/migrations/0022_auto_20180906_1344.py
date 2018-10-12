# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-06 13:44
from __future__ import unicode_literals

from django.db import migrations

from core.models import BasePage


def populate_service_for_existing_pages(apps, schema_migrations):
    for sub_class in BasePage.__subclasses__():
        try:
            historic_model = apps.get_model(
                    sub_class._meta.app_label, sub_class._meta.object_name
                )
        except LookupError:
            pass
        else:
            for page in historic_model.objects.all():
                page.service_name = sub_class.service_name_value
                page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20180904_1511'),
    ]

    operations = [
        migrations.RunPython(
            populate_service_for_existing_pages,
            reverse_code=migrations.RunPython.noop,
            elidable=True
        )
    ]
