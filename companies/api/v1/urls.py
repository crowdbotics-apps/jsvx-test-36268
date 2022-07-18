from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CompaniesViewSet

router = DefaultRouter()
router.register("companies", CompaniesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
