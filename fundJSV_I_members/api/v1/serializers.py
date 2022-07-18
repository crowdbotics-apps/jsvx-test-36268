from rest_framework import serializers
from fundJSV_I_members.models import FundJSV_I_members


class FundJSV_I_membersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundJSV_I_members
        fields = "__all__"
