from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('homepage.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admins/', include('admins.urls')),
]





handler404 = "dashboard.views.error_404_view"
