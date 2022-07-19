from django.conf import settings
from django.db import models


class Input_data(models.Model):
    "Generated Model"
    by_user = models.OneToOneField(
        "user_profile.Profile",
        on_delete=models.CASCADE,
        related_name="input_data_by_user",
    )
    data_in = models.URLField()
    data_to_company = models.OneToOneField(
        "company_name.Company_name",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="input_data_data_to_company",
    )


# Create your models here.
