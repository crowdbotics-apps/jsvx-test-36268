from django.conf import settings
from django.db import models


class Saved_data(models.Model):
    "Generated Model"
    database = models.ManyToManyField(
        "company_name.Company_name",
        related_name="saved_data_database",
    )


# Create your models here.
