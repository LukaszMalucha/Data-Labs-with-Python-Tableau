from django.urls import path
from .views import github_activity

app_name = "github_activity"

urlpatterns = [
    path('', github_activity, name="github_activity"),
    ]