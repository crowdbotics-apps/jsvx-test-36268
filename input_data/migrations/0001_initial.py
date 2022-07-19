# Generated by Django 2.2.26 on 2022-07-19 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_name', '0002_company_name_company_name'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_in', models.URLField()),
                ('by_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='input_data_by_user', to='user_profile.Profile')),
                ('data_to_company', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input_data_data_to_company', to='company_name.Company_name')),
            ],
        ),
    ]
