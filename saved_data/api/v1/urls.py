from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Saved_dataViewSet

router = DefaultRouter()
router.register("saved_data", Saved_dataViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
