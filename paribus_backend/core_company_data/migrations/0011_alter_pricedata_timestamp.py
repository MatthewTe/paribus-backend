# Generated by Django 4.1.4 on 2023-01-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_company_data', '0010_alter_pricedata_options_pricedata_daily_pct_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
