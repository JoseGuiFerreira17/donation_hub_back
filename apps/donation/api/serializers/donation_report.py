from rest_framework.serializers import ModelSerializer
from apps.donation.models import DonationReport


class DonationReportSerializer(ModelSerializer):
    class Meta:
        model = DonationReport
        fields = "__all__"
