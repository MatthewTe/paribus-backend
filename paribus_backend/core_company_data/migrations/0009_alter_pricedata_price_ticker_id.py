# Generated by Django 4.1.4 on 2023-01-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_company_data', '0008_pricedata_price_ticker_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='price_ticker_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
