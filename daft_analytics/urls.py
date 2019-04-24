from django.urls import path
from .views import daft_dashboard, price_estimator

app_name = "daft_analytics"

urlpatterns = [
    path('', daft_dashboard, name="daft_dashboard"),
    path('price_estimator', price_estimator, name="price_estimator"),
    ]