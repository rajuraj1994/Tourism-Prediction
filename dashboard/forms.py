from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm

from . import models
from .models import Profile, Booking


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user','username','email','ecard_no','ecard_cvv']


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['arrival_date', 'total_person']







