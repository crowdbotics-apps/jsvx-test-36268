from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FundJSV_I_membersViewSet

router = DefaultRouter()
router.register("fundjsv_i_members", FundJSV_I_membersViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
