from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='home_index'),
    path('login/', views.login, name='login'),
    path('register/', views.register),
    path('places/', views.place_list, name='country'),
    path('contact/', views.contact, name='contact'),
]




