from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Company_nameViewSet

router = DefaultRouter()
router.register("company_name", Company_nameViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
