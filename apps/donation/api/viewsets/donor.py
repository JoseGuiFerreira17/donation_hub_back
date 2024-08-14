from apps.core.api.viewsets import BaseModelViewSet
from apps.donation.api.filtersets import DonorFilterSet
from apps.donation.api.serializers import DonorDetailSerializer, DonorSerializer
from apps.donation.models import Donor


class DonorViewSet(BaseModelViewSet):
    model = Donor
    serializer_class = DonorSerializer
    filterset_class = DonorFilterSet
    action_serializer_classes = {
        "retrieve": DonorDetailSerializer,
    }
