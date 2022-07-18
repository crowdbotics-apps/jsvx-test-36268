from django.conf import settings
from django.db import models


class Fund(models.Model):
    "Generated Model"
    fundJSV_I = models.TextField()
    fundJSV_II = models.TextField()
    fundJSV_III = models.TextField()


# Create your models here.
