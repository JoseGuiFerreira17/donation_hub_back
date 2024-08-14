from django.contrib import admin
from apps.core.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "number", "complement", "neighborhood", "city", "state")
    search_fields = (
        "street",
        "number",
        "complement",
        "neighborhood",
        "city",
    )
