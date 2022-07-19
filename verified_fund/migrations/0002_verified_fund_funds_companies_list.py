# Generated by Django 2.2.26 on 2022-07-19 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('verified_fund', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verified_fund',
            name='funds_companies_list',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verified_fund_funds_companies_list', to='companies.Companies'),
        ),
    ]
