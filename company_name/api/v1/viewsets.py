from rest_framework import authentication
from company_name.models import Company_name
from .serializers import Company_nameSerializer
from rest_framework import viewsets


class Company_nameViewSet(viewsets.ModelViewSet):
    serializer_class = Company_nameSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Company_name.objects.all()
