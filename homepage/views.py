from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout
from . import forms, models
from .forms import SignupForm, ContactForms
from django.http import HttpResponse
from django.contrib import messages
from admins.models import Country, Places
from .auth import unauthenticated_user
from dashboard.models import Profile
from admins.filters import PlaceFilter


@unauthenticated_user
def index_page(request):
    context = {
        'activate_hhomepage': 'active border-bottom active-class',
    }
    return render(request, 'homepage/index.html', context)


# Accounts
@unauthenticated_user
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']
        user = auth.authenticate(username=uname, password=passwd)
        if user is not None:
            if not user.is_staff:
                auth.login(request, user)
                return redirect("/dashboard")

            elif user.is_staff:
                auth.login(request, user)
                return redirect('/admins')

        else:
            messages.error(request, "Invalid Login details! Unable to login")
            return render(request, 'homepage/login.html')

    else:
        return render(request, 'homepage/login.html')


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email=user.email)
            messages.add_message(request, messages.SUCCESS, "User has been created successfully!")
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, "Failed to create an account, Check carefully and Try Again!")
            return render(request, 'homepage/register.html', {'form': form})
    context = {
        'form': SignupForm
    }
    return render(request, 'homepage/register.html', context)


@unauthenticated_user
def place_list(request):
    data = Places.objects.all().order_by('-id')
    filter = PlaceFilter(request.GET, queryset=data)
    filtered_data = filter.qs
    context = {
        'results': filtered_data,
        'filter': filter,
        'activate_hcountry': 'active border-bottom active-class'
    }
    return render(request, 'homepage/country.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Contact form has been submitted")
            return redirect('/contact')
        else:
            messages.add_message(request, messages.ERROR, "Error")
            return render(request, 'homepage/contact.html', {'form':form})
    context = {
        'form': ContactForms
    }
    return render(request, 'homepage/contact.html', context)



