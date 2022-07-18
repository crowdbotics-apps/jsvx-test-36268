from django.conf import settings
from django.db import models


class FundJSV_I_members(models.Model):
    "Generated Model"
    member_I = models.OneToOneField(
        "fund.Fund",
        on_delete=models.CASCADE,
        related_name="fundjsv_i_members_member_I",
    )
    member_II = models.OneToOneField(
        "fund.Fund",
        on_delete=models.CASCADE,
        related_name="fundjsv_i_members_member_II",
    )
    member_III = models.OneToOneField(
        "fund.Fund",
        on_delete=models.CASCADE,
        related_name="fundjsv_i_members_member_III",
    )
    member_IV = models.OneToOneField(
        "fund.Fund",
        on_delete=models.CASCADE,
        related_name="fundjsv_i_members_member_IV",
    )
    member_V = models.OneToOneField(
        "fund.Fund",
        on_delete=models.CASCADE,
        related_name="fundjsv_i_members_member_V",
    )


# Create your models here.
