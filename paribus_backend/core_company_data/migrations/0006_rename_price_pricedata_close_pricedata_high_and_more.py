# Generated by Django 4.1.4 on 2022-12-31 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_company_data', '0005_companycore_ticker_pricedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricedata',
            old_name='price',
            new_name='close',
        ),
        migrations.AddField(
            model_name='pricedata',
            name='high',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricedata',
            name='low',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricedata',
            name='open',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]
