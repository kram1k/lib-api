from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LibraryViewSet

app_name = "api"

router = DefaultRouter()

router.register(r"lib", LibraryViewSet, basename="library")

urlpatterns = [
    path("", include(router.urls)),
]
