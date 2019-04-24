from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views_user, views_algorithm

app_name = 'api'

router = DefaultRouter()
# router.register('courses', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('create/', views_user.CreateUserView.as_view(), name='create'),
    path('authenticate/', views_user.CreateTokenView.as_view(), name='authenticate'),
    path('my_account/', views_user.ManageUserView.as_view(), name='my_account'),
    path('estimate_property/', views_algorithm.EstimatePropertyView.as_view(), name='estimate_property'),
    path('test_profile/', views_algorithm.TestProfileView.as_view(), name='test_profile')
]
