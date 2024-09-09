from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class CountryFormCSV(ModelForm):
    class Meta:
        model = CountryCSV
        fields = '__all__'


class ArrivalForm(ModelForm):
    class Meta:
        model = ArrivalCSV
        fields = '__all__'


class ExpenditureForm(ModelForm):
    class Meta:
        model = ExpenditureCSV
        fields = '__all__'


class PlaceForm(ModelForm):
    class Meta:
        model = Places
        fields = '__all__'
        exclude = ['total_rating', 'total_comments']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'rating']


class AddAdmin(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']







