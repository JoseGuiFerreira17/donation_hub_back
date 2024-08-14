from rest_framework.serializers import ModelSerializer
from apps.donation.models import Donation
from apps.organization.api.serializers import OrganizationSerializer


class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"


class DonationDetailSerializer(ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Donation
        fields = "__all__"
