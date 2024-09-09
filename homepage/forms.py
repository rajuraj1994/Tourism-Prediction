from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import ContactForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ContactForms(ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'



