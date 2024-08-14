from django_filters.rest_framework import FilterSet
from apps.accounts.models import User


class UserFilterSet(FilterSet):
    class Meta:
        model = User
        fields = {
            "id": ["exact"],
            "name": ["exact", "icontains"],
            "email": ["exact", "icontains"],
            "phone": ["exact", "icontains"],
            "is_active": ["exact"],
            "is_staff": ["exact"],
            "created_at": ["exact", "lt", "gt", "lte", "gte"],
            "modified_at": ["exact", "lt", "gt", "lte", "gte"],
        }
