from rest_framework import authentication
from fund.models import Fund
from .serializers import FundSerializer
from rest_framework import viewsets


class FundViewSet(viewsets.ModelViewSet):
    serializer_class = FundSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Fund.objects.all()
