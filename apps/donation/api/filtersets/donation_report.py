from django_filters.rest_framework import FilterSet
from apps.donation.models import DonationReport


class DonationReportFilterSet(FilterSet):
    class Meta:
        model = DonationReport
        fields = {
            "title": ["exact", "icontains"],
            "format": ["exact"],
            "file_path": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
