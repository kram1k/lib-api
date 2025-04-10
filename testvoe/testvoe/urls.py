from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/swagger-ui/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
    path("api/docs/redoc/", SpectacularRedocView.as_view(), name="redoc"),
]
