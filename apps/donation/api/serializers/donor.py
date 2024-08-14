from rest_framework.serializers import ModelSerializer
from apps.donation.models import Donor
from apps.core.api.serializers import AddressSerializer


class DonorSerializer(ModelSerializer):
    class Meta:
        model = Donor
        fields = "__all__"


class DonorDetailSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Donor
        fields = "__all__"
