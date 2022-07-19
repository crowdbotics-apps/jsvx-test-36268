from django.conf import settings
from django.db import models


class Verified_fund(models.Model):
    "Generated Model"
    company_name = models.TextField()
    location = models.TextField()
    employees = models.OneToOneField(
        "user_profile.Profile",
        on_delete=models.CASCADE,
        related_name="verified_fund_employees",
    )


# Create your models here.
