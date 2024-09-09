from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_page),
    path('place_details/<str:place_id>', views.place_details, name="place_details"),
    path('booking/<int:place_id>', views.booking, name="booking"),
    path('show_booking', views.show_booking, name="show_booking"),
    path('trending_places', views.trending_places, name="trending"),

    path('logout/', views.logout_view),
    path('profile/', views.profile, name='profile'),

    path('show_country', views.show_country, name="show_country_user"),
    path('show_country_by_arrival', views.show_country_by_arrival, name="show_country_by_arr"),
    path('show_country_by_expenditure', views.show_country_by_expenditure, name="show_country_by_exp"),
    path('show_details_arrival/<str:arrival_id>', views.show_details_arrival, name='show_details_arrival_user'),
    path('show_details_expenditure/<str:arrival_id>', views.show_details_expenditure, name='show_details_expenditure_user'),

    path('settings', views.password_change, name='password_change'),
    path('cancel_booking/<str:id>', views.cancel_booking, name='cancel_booking'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


