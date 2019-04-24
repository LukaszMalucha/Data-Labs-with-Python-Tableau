from django.urls import path, include
from .views import ds_dashboard, data_skillset,results

urlpatterns = [
    path('ds_dashboard', ds_dashboard, name="ds_dashboard"),
    path('data_skillset', data_skillset, name="data_skillset"),
    path('results', results, name="results"),
    ]