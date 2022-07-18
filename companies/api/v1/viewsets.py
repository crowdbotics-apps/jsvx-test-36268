from rest_framework import authentication
from companies.models import Companies
from .serializers import CompaniesSerializer
from rest_framework import viewsets


class CompaniesViewSet(viewsets.ModelViewSet):
    serializer_class = CompaniesSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Companies.objects.all()
