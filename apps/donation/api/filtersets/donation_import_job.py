from django_filters.rest_framework import FilterSet
from apps.donation.models import DonationImportJob


class DonationImportJobFilterSet(FilterSet):
    class Meta:
        model = DonationImportJob
        fields = {
            "file_path": ["exact", "icontains"],
            "status": ["exact"],
            "created_at": ["exact", "gte", "lte"],
        }
