# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-24 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0033_auto_20181023_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlelistingpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deprecatedgetfinancepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='euexitdomesticformpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='euexitformsuccesspage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='euexitinternationalformpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exportreadinessapp',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='internationallandingpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newgetfinancepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='performancedashboardnotespage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='performancedashboardpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='privacyandcookiespage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='termsandconditionspage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='topiclandingpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True),
        ),
    ]