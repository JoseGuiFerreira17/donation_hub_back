from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.organization.api.viewsets import OrganizationViewSet


router = SimpleRouter()

router.register("organizations", OrganizationViewSet, basename="organizations")

urlpatterns = [
    path("", include(router.urls)),
]
