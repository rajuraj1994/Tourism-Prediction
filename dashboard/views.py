from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from admins.models import *
from admins.filters import *
from admins.forms import *
from dashboard.models import Profile, Booking
from homepage.auth import user_only
from .forms import ProfileForm, BookingForm
from django.http import JsonResponse

import io, csv, pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



@login_required(login_url='login')
@user_only
def index_page(request):
    data = Places.objects.all().order_by('-id')
    filter = PlaceFilter(request.GET, queryset=data)
    filtered_data = filter.qs
    context = {
        'results': filtered_data,
        'filter': filter,
        'activate_adminhome': 'active bg-primary',
        'activate_home': 'active border-bottom active-class'
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='login')
@user_only
def trending_places(request):
    data = Places.objects.all().order_by('-total_comments', '-total_rating')[:20]
    context = {
        'results': data,
        'activate_trending': 'active bg-primary',
    }
    return render(request, 'dashboard/trending.html', context)


@login_required(login_url='login')
@user_only
def place_details(request, place_id):
    data = Places.objects.get(id=place_id)
    comments = Comment.objects.filter(place=data.id).order_by('-id')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            userdata = form.save()
            userdata.user = request.user
            userdata.place = data
            userdata.save()
            data.total_rating = int(data.total_rating) + int(userdata.rating)
            data.total_comments = data.total_comments + 1
            data.save()
            if userdata:
                messages.add_message(request, messages.SUCCESS, 'Comment added successfully')
                return redirect('/dashboard/place_details/'+str(data.id))
            else:
                context = {
                    'results': data,
                    'comments': comments,
                    'form': form,
                    'activate_adminhome': 'active bg-primary',
                }
                return render(request, 'dashboard/place_details.html', context)
    context = {
        'results': data,
        'comments': comments,
        'form': CommentForm,
        'activate_adminhome': 'active bg-primary',
    }
    return render(request, 'dashboard/place_details.html', context)


@login_required(login_url='login')
@user_only
def booking(request, place_id):
    data = Places.objects.get(id=place_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            userdata = form.save()
            userdata.user = request.user
            userdata.place = data
            userdata.status = 'Pending'
            userdata.save()
            if userdata:
                messages.add_message(request, messages.SUCCESS, 'Booked successfully')
                return redirect('/dashboard/show_booking')
            else:
                context = {
                    'results': data,
                    'form': form,
                    'activate_adminhome': 'active bg-primary',
                }
                return render(request, 'dashboard/booking.html', context)
    context = {
        'results': data,
        'form': BookingForm,
        'activate_adminhome': 'active bg-primary',
    }
    return render(request, 'dashboard/booking.html', context)


@login_required(login_url='login')
@user_only
def show_booking(request):
    data = Booking.objects.filter(user=request.user).order_by('-id')
    context = {
        'results': data,
        'activate_booking': 'active bg-primary',
    }
    return render(request, 'dashboard/summary.html', context)


@login_required(login_url='login')
@user_only
def cancel_booking(request, id):
    country = Booking.objects.get(id=id)
    country.delete()
    messages.add_message(request, messages.SUCCESS, 'Booking cancelled successfully')
    return redirect('/dashboard/show_booking')


@login_required(login_url='login')
@user_only
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
@user_only
def show_country(request):
    results = Country.objects.all().values('country_name', 'country_code', 'id').distinct()
    result_filter = CountryFilter(request.GET, queryset=results)
    result_final = result_filter.qs
    context = {
        'results': result_final,
        'result_filter': result_filter,
        'activate_country': 'active bg-primary'
    }
    return render(request, 'dashboard/show_country.html',context)

@login_required(login_url='login')
@user_only
def show_country_by_arrival(request):
    results = Arrival.objects.all()
    result_filter = ArrivalFilter(request.GET, queryset=results)
    result_final = result_filter.qs
    context = {
        'results': result_final,
        'result_filter': result_filter,
        'activate_country_arrival': 'active bg-primary'
    }
    return render(request, 'dashboard/show_country_by_arrival.html',context)


@login_required(login_url='login')
@user_only
def show_details_arrival(request, arrival_id):
    results = Arrival.objects.get(id=arrival_id)
    result_data = pd.read_csv('static/data/TestData.csv')
    X = result_data.drop(['id', 'target'], axis=1)
    Y = result_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2)
    model = LinearRegression()
    model.fit(X_train, Y_train)
    input_data = (results.a2017, results.a2018, results.a2019, results.a2020, results.a2021)
    input_data_as_numpy_array2 = np.asarray(input_data)
    input_date_reshaped = input_data_as_numpy_array2.reshape(1, -1)
    prediction = round(model.predict(input_date_reshaped)[0],0)
    context = {
        'results': results,
        'prediction': prediction,
        'activate_country_arrival': 'active bg-primary'
    }
    return render(request, 'dashboard/show_details_arrival.html',context)


@login_required(login_url='login')
@user_only
def show_country_by_expenditure(request):
    results = Expenditure.objects.all()
    result_filter = ExpenditureFilter(request.GET, queryset=results)
    result_final = result_filter.qs
    context = {
        'results': result_final,
        'result_filter': result_filter,
        'activate_country_expenditure': 'active bg-primary'
    }
    return render(request, 'dashboard/show_country_by_expenditure.html',context)


@login_required(login_url='login')
@user_only
def show_details_expenditure(request, arrival_id):
    results = Expenditure.objects.get(id=arrival_id)
    result_data = pd.read_csv('static/data/TestData.csv')
    X = result_data.drop(['id', 'target'], axis=1)
    Y = result_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=2)
    model = LinearRegression()
    model.fit(X_train, Y_train)

    input_data = (results.e2017, results.e2018, results.e2019, results.e2020, results.e2021)
    input_data_as_numpy_array2 = np.asarray(input_data)
    input_date_reshaped = input_data_as_numpy_array2.reshape(1, -1)
    prediction = round(model.predict(input_date_reshaped)[0],2)
    context = {
        'results': results,
        'prediction': prediction,
        'activate_country_expenditure': 'active bg-primary'
    }
    return render(request, 'dashboard/show_details_expenditure.html',context)


@login_required(login_url='login')
@user_only
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile has been refined successfully!')
            return redirect('/dashboard/profile')
    context = {
        'form': ProfileForm(instance=profile),
        'activate_profile': 'active bg-primary'
    }
    return render(request, 'dashboard/profile.html', context)


def error_404_view(request, exception):
    return render(request, '404.html')


@login_required(login_url='login')
@user_only
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, 'Password Changed Successfully')
            return redirect('/dashboard/profile')

        else:
            messages.add_message(request, messages.ERROR, 'Please verify the form fields')
            return render(request, 'dashboard/password_change.html', {'form':form})
    context = {
        'form':PasswordChangeForm(request.user),
        'activate_settings':'active bg-primary'
    }
    return render(request, 'dashboard/password_change.html', context)


