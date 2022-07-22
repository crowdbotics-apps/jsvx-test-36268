from rest_framework import authentication
from saved_data.models import Saved_data
from .serializers import Saved_dataSerializer
from rest_framework import viewsets


class Saved_dataViewSet(viewsets.ModelViewSet):
    serializer_class = Saved_dataSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Saved_data.objects.all()
