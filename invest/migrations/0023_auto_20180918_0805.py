# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 08:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0022_auto_20180917_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highpotentialopportunityformpage',
            name='terms_agreed_help_text',
        ),
        migrations.RemoveField(
            model_name='highpotentialopportunityformpage',
            name='terms_agreed_label',
        ),
    ]