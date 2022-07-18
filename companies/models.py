from django.conf import settings
from django.db import models


class Companies(models.Model):
    "Generated Model"
    company = models.CharField(
        max_length=256,
    )


# Create your models here.
