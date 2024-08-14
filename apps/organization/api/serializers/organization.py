from rest_framework.serializers import ModelSerializer
from apps.core.api.serializers import AddressSerializer
from apps.organization.models import Organization


class OrganizationDetailSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Organization
        fields = "__all__"


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
