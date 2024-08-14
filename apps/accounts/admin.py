from django.contrib import admin
from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "is_active", "is_staff"]
    list_filter = ["is_active", "is_staff", "created_at", "modified_at"]
    search_fields = ["name", "email", "phone"]
    fieldsets = (
        ("Informações Básicas", {"fields": ("name", "email", "phone")}),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        ("Datas", {"fields": ("created_at", "modified_at")}),
    )
    ordering = ["-created_at"]

    actions = ["activate_users", "deactivate_users"]

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    activate_users.short_description = "Activate selected users"

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_users.short_description = "Deactivate selected users"
