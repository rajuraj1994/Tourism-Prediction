import django_filters
from dashboard.models import *
from .models import *
from django.contrib.auth.models import User
from django_filters import CharFilter



class UserFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains')
    email = CharFilter(field_name='email', lookup_expr='icontains')
    class Meta:
        model = User
        fields = ''


class BookingFilter(django_filters.FilterSet):
    place_name = CharFilter(field_name='place__place_name', lookup_expr='icontains')
    class Meta:
        model = Booking
        fields = ['status']


class CountryFilter(django_filters.FilterSet):
    country_name = CharFilter(field_name='country_name', lookup_expr='icontains')
    country_code = CharFilter(field_name='country_code', lookup_expr='icontains')

    class Meta:
        model = Country
        fields = ''


class ArrivalFilter(django_filters.FilterSet):
    country_name = CharFilter(field_name='country_name', lookup_expr='icontains')
    country_code = CharFilter(field_name='country_code', lookup_expr='icontains')

    class Meta:
        model = Arrival
        fields = ''


class ExpenditureFilter(django_filters.FilterSet):
    country_name = CharFilter(field_name='country_name', lookup_expr='icontains')
    country_code = CharFilter(field_name='country_code', lookup_expr='icontains')

    class Meta:
        model = Expenditure
        fields = ''


class PlaceFilter(django_filters.FilterSet):
    place_name = CharFilter(field_name='place_name', lookup_expr='icontains')

    class Meta:
        model = Places
        fields = ''


