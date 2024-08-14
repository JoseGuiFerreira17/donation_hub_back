from django_filters.rest_framework import FilterSet
from apps.donation.models import Donation


class DonationFilterSet(FilterSet):
    class Meta:
        model = Donation
        fields = {
            "amount": ["exact", "gte", "lte"],
            "date": ["exact", "gte", "lte"],
            "organization__name": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
