# Generated by Django 4.1.4 on 2022-12-31 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_company_data', '0003_companycore_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='companycore',
            name='is_public',
            field=models.BooleanField(blank=True, default=None),
            preserve_default=False,
        ),
    ]
