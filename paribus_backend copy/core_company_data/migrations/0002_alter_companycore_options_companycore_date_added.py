# Generated by Django 4.1.4 on 2022-12-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_company_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companycore',
            options={'verbose_name': 'Core Company Metadata', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AddField(
            model_name='companycore',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]