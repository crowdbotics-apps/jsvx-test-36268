from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FundViewSet

router = DefaultRouter()
router.register("fund", FundViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
