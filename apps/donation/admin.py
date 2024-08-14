from django.contrib import admin
from apps.donation.models import Donor, Donation, DonationReport, DonationImportJob


admin.site.register(Donor)


class DonorAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone"]
    search_fields = ["name", "email", "phone"]


admin.site.register(Donation)


class DonationAdmin(admin.ModelAdmin):
    list_display = ["amount", "donor", "date", "organization", "notes", "created_at"]
    search_fields = ["amount", "notes"]


admin.site.register(DonationReport)


class DonationReportAdmin(admin.ModelAdmin):
    list_display = ["title", "format", "file_path", "created_at"]
    search_fields = ["title", "format", "file_path"]


admin.site.register(DonationImportJob)


class DonationImportJobAdmin(admin.ModelAdmin):
    list_display = ["file_path", "status", "created_at"]
    search_fields = ["file_path", "status", "created_at"]
