from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path("test-profile/", views.TestProfileView.as_view(), name="test-profile"),
]
