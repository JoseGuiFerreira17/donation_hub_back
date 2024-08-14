from apps.core.api.viewsets import BaseModelViewSet
from apps.donation.api.filtersets import DonationReportFilterSet
from apps.donation.api.serializers import DonationReportSerializer
from apps.donation.models import DonationReport


class DonationReportViewSet(BaseModelViewSet):
    model = DonationReport
    serializer_class = DonationReportSerializer
    filterset_class = DonationReportFilterSet
