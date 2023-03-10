# Generated by Django 4.1.4 on 2022-12-31 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_company_data', '0004_companycore_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='companycore',
            name='ticker',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='PriceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField()),
                ('price', models.FloatField()),
                ('volume', models.PositiveIntegerField()),
                ('market_cap', models.BigIntegerField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_company_data.companycore')),
            ],
            options={
                'verbose_name': 'Company Price Timeseries',
            },
        ),
    ]
