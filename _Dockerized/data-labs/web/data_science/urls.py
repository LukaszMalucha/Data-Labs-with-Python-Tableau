from django.urls import path
from .views import ds_dashboard, test_profile

app_name = "data_science"

urlpatterns = [
    path('ds_dashboard', ds_dashboard, name="ds_dashboard"),
    path('test_profile', test_profile, name="test_profile"),
]
