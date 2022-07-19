from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Input_dataViewSet

router = DefaultRouter()
router.register("input_data", Input_dataViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
