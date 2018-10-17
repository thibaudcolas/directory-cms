# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 13:46
from __future__ import unicode_literals

import core.api_fields
import core.fields
import core.models
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('core', '0019_merge_20180829_0939'),
        ('export_readiness', '0013_exportreadinessapp_service_name'),
        ('wagtailimages', '0021_image_file_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exportreadinessapp',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True),
        ),
        migrations.RenameModel(
            old_name='GetFinancePage',
            new_name='DeprecatedGetFinancePage',
        ),
        migrations.CreateModel(
            name='NewGetFinancePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('hero_text', core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('contact_proposition', core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('contact_button', models.CharField(max_length=500)),
                ('advantages_title', models.CharField(max_length=500)),
                ('advantages_one', core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('advantages_two', core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('advantages_three', core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('evidence', core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('evidence_video_embed', models.CharField(max_length=500)),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('ukef_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page', models.Model),
        ),
    ]
