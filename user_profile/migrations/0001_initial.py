# Generated by Django 2.2.26 on 2022-07-19 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_photo", models.URLField()),
                ("user_contact", models.TextField()),
                ("users_verified_fund", models.TextField(blank=True, null=True)),
                (
                    "first_last_name",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_first_last_name",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
