from rest_framework import authentication
from input_data.models import Input_data
from .serializers import Input_dataSerializer
from rest_framework import viewsets


class Input_dataViewSet(viewsets.ModelViewSet):
    serializer_class = Input_dataSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Input_data.objects.all()
