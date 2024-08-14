from apps.core.api.viewsets import BaseModelViewSet
from apps.organization.api.filtersets import OrganizationFilterSet
from apps.organization.api.serializers import (
    OrganizationSerializer,
    OrganizationDetailSerializer,
)
from apps.organization.models import Organization


class OrganizationViewSet(BaseModelViewSet):
    model = Organization
    serializer_class = OrganizationSerializer
    filterset_class = OrganizationFilterSet
    action_serializer_classes = {
        "retrieve": OrganizationDetailSerializer,
    }
