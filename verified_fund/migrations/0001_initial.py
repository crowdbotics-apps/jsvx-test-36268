# Generated by Django 2.2.26 on 2022-07-19 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verified_fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField()),
                ('location', models.TextField()),
                ('employees', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='verified_fund_employees', to='user_profile.Profile')),
            ],
        ),
    ]
