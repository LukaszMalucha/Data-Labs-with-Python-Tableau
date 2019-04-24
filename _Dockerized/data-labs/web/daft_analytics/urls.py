from django.urls import path
from .views import daft_dashboard, price_estimator, city_choice

app_name = "daft_analytics"

urlpatterns = [
    path('', daft_dashboard, name="daft_dashboard"),
    path('price_estimator', price_estimator, name="price_estimator"),
    path('city_choice', city_choice, name="city_choice"),
    ]