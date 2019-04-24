from django.contrib import admin
from django.urls import path, include

from dashboard.views import error_404, error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('user/', include('user.urls')),
    path('life_expectancy/', include('life_expectancy.urls')),
    path('github_activity/', include('github_activity.urls')),
    path('data_science/', include('data_science.urls')),
    path('daft_analytics/', include('daft_analytics.urls')),
    path('api/', include('api.urls')),
]


handler404 = error_404
handler500 = error_500