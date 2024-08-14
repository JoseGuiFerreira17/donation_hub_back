from django_filters.rest_framework import FilterSet
from apps.donation.models import Donor


class DonorFilterSet(FilterSet):
    class Meta:
        model = Donor
        fields = {
            "name": ["exact", "icontains"],
            "email": ["exact", "icontains"],
            "phone": ["exact", "icontains"],
            "address__city": ["exact", "icontains"],
            "address__state": ["exact"],
        }
