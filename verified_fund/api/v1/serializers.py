from rest_framework import serializers
from verified_fund.models import Verified_fund


class Verified_fundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verified_fund
        fields = "__all__"
