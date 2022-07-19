from rest_framework import authentication
from verified_fund.models import Verified_fund
from .serializers import Verified_fundSerializer
from rest_framework import viewsets


class Verified_fundViewSet(viewsets.ModelViewSet):
    serializer_class = Verified_fundSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Verified_fund.objects.all()
