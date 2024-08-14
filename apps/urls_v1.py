from django.urls import path, include


urlpatterns = [
    path("", include("apps.docs_url")),
    path("", include("apps.accounts.api.routers")),
    path("", include("apps.organization.api.routers")),
    path("", include("apps.donation.api.routers")),
]
