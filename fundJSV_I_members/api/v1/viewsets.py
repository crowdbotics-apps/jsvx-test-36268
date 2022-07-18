from rest_framework import authentication
from fundJSV_I_members.models import FundJSV_I_members
from .serializers import FundJSV_I_membersSerializer
from rest_framework import viewsets


class FundJSV_I_membersViewSet(viewsets.ModelViewSet):
    serializer_class = FundJSV_I_membersSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = FundJSV_I_members.objects.all()
