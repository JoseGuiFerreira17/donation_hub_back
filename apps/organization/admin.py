from django.contrib import admin
from apps.organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "email", "phone")
    fields = (
        "name",
        "cnpj",
        "email",
        "phone",
        "address",
        "foundation_date",
        "website",
        "is_active",
    )
    actions = ["make_active", "make_inactive"]

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = "Mark selected organizations as active"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = "Mark selected organizations as inactive"
