from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path("user/", views.CurrentUserApiView.as_view(), name="current-user"),
    path('test-profile/', views.TestProfileView.as_view(), name='test-profile'),
    path('estimate-property/', views.EstimatePropertyView.as_view(), name='estimate-property')
]
