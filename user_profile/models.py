from django.conf import settings
from django.db import models


class Profile(models.Model):
    "Generated Model"
    first_last_name = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="profile_first_last_name",
    )
    user_photo = models.URLField()
    user_contact = models.TextField()
    users_verified_fund = models.TextField(
        null=True,
        blank=True,
    )


# Create your models here.
