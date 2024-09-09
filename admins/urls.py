from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('addcountry_csv/', views.add_country_csv, name='add_country_csv'),
    path('addcountry_manual/', views.add_country_manual, name='add_country_manual'),
    path('show_country', views.show_country),
    path('delete_country/<str:country_id>', views.delete_country, name='delete_country'),
    path('delete_all_country', views.delete_all_country, name='delete_all_country'),

    path('addarrival_csv/', views.add_arrival_csv, name='add_arrival_csv'),
    path('addexpenditure_csv/', views.add_expenditure_csv, name='add_expenditure_csv'),

    path('show_country_by_arrival', views.show_country_by_arrival),
    path('delete_arrival/<str:country_id>', views.delete_arrival, name='delete_arrival'),
    path('delete_all_arrival', views.delete_all_arrival, name='delete_all_arrival'),

    path('show_country_by_expenditure', views.show_country_by_expenditure),
    path('delete_expenditure/<str:country_id>', views.delete_expenditure, name='delete_expenditure'),
    path('delete_all_expenditure', views.delete_all_expenditure, name='delete_all_expenditure'),

    path('show_details_arrival/<str:arrival_id>', views.show_details_arrival, name='show_details_arrival'),
    path('show_details_expenditure/<str:arrival_id>', views.show_details_expenditure, name='show_details_expenditure'),

    path('addplace/', views.add_place, name="add_place"),
    path('showplace/', views.show_place, name="show_place"),
    path('deleteplace/<str:id>', views.delete_place, name='delete_place'),
    path('show_details_place/<str:id>', views.show_details_place, name="show_details_place"),
    path('update_place/<str:id>', views.update_place, name="update_place"),

    path('showusers/', views.show_users),
    path('showadmins/', views.show_admins),
    path('delete_user/<int:user_id>', views.delete_user, name='delete_user'),
    path('delete_admin/<int:user_id>', views.delete_admin, name='delete_admin'),


    path('bookingdata/', views.booking_data),
    path('confirm_booking/<str:id>', views.confirm_booking, name="confirm_booking"),
    path('deny_booking/<str:id>', views.deny_booking, name="deny_booking"),

    path('addadmin/', views.add_admin),

    path('contact/', views.contact_form),
    path('logout/', views.logout_view),
]


