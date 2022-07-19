from rest_framework import serializers
from input_data.models import Input_data


class Input_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input_data
        fields = "__all__"
