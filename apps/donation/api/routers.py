from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.donation.api.viewsets import (
    DonationViewSet,
    DonationReportViewSet,
    DonationImportJobViewSet,
    DonorViewSet,
)


router = SimpleRouter()

router.register("donations", DonationViewSet, basename="donations")
router.register("donation-reports", DonationReportViewSet, basename="donation-reports")
router.register(
    "donation-import-jobs", DonationImportJobViewSet, basename="donation-import-jobs"
)
router.register("donors", DonorViewSet, basename="donors")

urlpatterns = [
    path("", include(router.urls)),
]
