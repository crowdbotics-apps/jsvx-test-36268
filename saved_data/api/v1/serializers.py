from rest_framework import serializers
from saved_data.models import Saved_data


class Saved_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved_data
        fields = "__all__"
