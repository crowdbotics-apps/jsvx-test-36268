from django.conf import settings
from django.db import models


class Company(models.Model):
    "Generated Model"
    companyname = models.OneToOneField(
        "companies.Companies",
        on_delete=models.CASCADE,
        related_name="company_companyname",
    )
    fund = models.TextField()
    status = models.TextField()
    investedinitially = models.BigIntegerField()
    totalcapitalinvested_JSV_Main = models.BigIntegerField()
    totalcapitalinvested_JSA_Side = models.BigIntegerField()
    totalcapitalinvested_JSV_JSA = models.BigIntegerField()
    totalcapitalraised = models.BigIntegerField()
    initialvaluation = models.BigIntegerField()
    realizedreturn = models.BigIntegerField()
    totalvalue = models.BigIntegerField()
    total_GainLoss = models.BigIntegerField()
    deallevelIRR = models.BigIntegerField()
    deallevelMOIC = models.BigIntegerField()


# Create your models here.
