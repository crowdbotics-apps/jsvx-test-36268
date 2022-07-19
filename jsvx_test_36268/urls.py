"""jsvx_test_36268 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("modules/", include("modules.urls")),
    path("api/v1/", include("home.api.v1.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("rest-auth/", include("rest_auth.urls")),
    # Override email confirm to use allauth's HTML view instead of rest_auth's API view
    path("rest-auth/registration/account-confirm-email/<str:key>/", confirm_email),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("api/v1/", include("companies.api.v1.urls")),
    path("api/v1/", include("company.api.v1.urls")),
    path("api/v1/", include("fund.api.v1.urls")),
    path("api/v1/", include("fundJSV_I_members.api.v1.urls")),
    path("companies/", include("companies.urls")),
    path("company/", include("company.urls")),
    path("api/v1/", include("company_name.api.v1.urls")),
    path("fund/", include("fund.urls")),
    path("fundJSV_I_members/", include("fundJSV_I_members.urls")),
    path("company_name/", include("company_name.urls")),
    path("api/v1/", include("user_profile.api.v1.urls")),
    path("api/v1/", include("verified_fund.api.v1.urls")),
    path("api/v1/", include("input_data.api.v1.urls")),
    path("input_data/", include("input_data.urls")),
    path("user_profile/", include("user_profile.urls")),
    path("verified_fund/", include("verified_fund.urls")),
]

admin.site.site_header = "JSVX Test"
admin.site.site_title = "JSVX Test Admin Portal"
admin.site.index_title = "JSVX Test Admin"

# swagger
api_info = openapi.Info(
    title="JSVX Test API",
    default_version="v1",
    description="API documentation for JSVX Test App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]
