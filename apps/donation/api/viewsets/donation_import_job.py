from apps.core.api.viewsets import BaseModelViewSet
from apps.donation.api.filtersets import DonationImportJobFilterSet
from apps.donation.api.serializers import DonationImportJobSerializer
from apps.donation.models import DonationImportJob


class DonationImportJobViewSet(BaseModelViewSet):
    model = DonationImportJob
    serializer_class = DonationImportJobSerializer
    filterset_class = DonationImportJobFilterSet
