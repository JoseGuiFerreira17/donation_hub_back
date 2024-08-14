from apps.core.api.viewsets import BaseModelViewSet
from apps.donation.api.filtersets import DonationFilterSet
from apps.donation.api.serializers import DonationDetailSerializer, DonationSerializer
from apps.donation.models import Donation


class DonationViewSet(BaseModelViewSet):
    model = Donation
    serializer_class = DonationSerializer
    filterset_class = DonationFilterSet
    action_serializer_classes = {
        "retrieve": DonationDetailSerializer,
    }
