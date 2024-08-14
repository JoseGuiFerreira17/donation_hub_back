from django_filters.rest_framework import FilterSet
from apps.organization.models import Organization


class OrganizationFilterSet(FilterSet):

    class Meta:
        model = Organization
        fields = {
            "name": ["icontains"],
            "email": ["icontains"],
            "phone": ["icontains"],
            "address__state": ["exact"],
            "address__city": ["exact"],
        }
