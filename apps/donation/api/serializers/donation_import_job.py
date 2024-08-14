from rest_framework.serializers import ModelSerializer
from apps.donation.models import DonationImportJob


class DonationImportJobSerializer(ModelSerializer):
    class Meta:
        model = DonationImportJob
        fields = "__all__"
