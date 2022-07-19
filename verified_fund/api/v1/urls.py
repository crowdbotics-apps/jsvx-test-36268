from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Verified_fundViewSet

router = DefaultRouter()
router.register("verified_fund", Verified_fundViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
