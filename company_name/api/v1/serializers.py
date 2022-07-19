from rest_framework import serializers
from company_name.models import Company_name


class Company_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_name
        fields = "__all__"
