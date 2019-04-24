from django.urls import path
from .views import life_expectancy

app_name = "life_expectancy"

urlpatterns = [
    path('', life_expectancy, name="life_expectancy"),
    ]