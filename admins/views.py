from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *
from homepage.auth import *
from dashboard.models import *
from homepage.models import *
from .filters import *
from .models import *


import io, csv, pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression


@login_required(login_url='login')
@admin_only
def add_country_csv(request):
    if request.method == 'POST':
        file = request.FILES['file']
        reader = pd.read_csv(file, on_bad_lines='skip')
        reader.fillna(0, inplace=True)
        for _, row in reader.iterrows():
            new_file = Country(
                country_name=row['Country Name'],
                country_code=row['Country Code'],
            )
            new_file.save()
        messages.add_message(request, messages.SUCCESS, 'Country Added Successfully.')
        return redirect('/admins/show_country')
    context = {
        'form': CountryFormCSV,
        'activate_country': 'active bg-primary'
    }
    return render(request, 'admins/add_country_csv.html', context)


@login_required(login_url='login')
@admin_only
def add_country_manual(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Country Added Successfully.')
            return redirect('/admins/show_country')
        else:
            messages.add_message(request, messages.ERROR, "Please check form fields")
            return render(request, 'admins/add_country_manual.html', {'form':form})
    context = {
        'form': CountryForm,
        'activate_country': 'active bg-primary'
    }
    return render(request, 'admins/add_country_manual.html', context)


@login_required(login_url='login')
@admin_only
def show_country(request):
    results = Country.objects.all().values('country_name', 'country_code', 'id').distinct()
    result_filter = CountryFilter(request.GET, queryset=results)
    result_final = result_filter.qs
    context = {
        'results': result_final,
        'result_filter': result_filter,
        'activate_country': 'active bg-primary'
    }
    return render(request, 'admins/show_country.html',context)


@login_required(login_url='login')
@admin_only
def delete_country(request, country_id):
    country = Country.objects.get(id=country_id)
    country.delete()
    messages.add_message(request, messages.SUCCESS, 'Country deleted successfully')
    return redirect('/admins/show_country')


@login_required(login_url='login')
@admin_only
def delete_all_country(request):
    country = Country.objects.all()
    country.delete()
    messages.add_message(request, messages.SUCCESS, 'All countries deleted successfully')
    return redirect('/admins/show_country')


@login_required(login_url='login')
@admin_only
def add_arrival_csv(request):
    if request.method == 'POST':
        file = request.FILES['file']
        reader = pd.read_csv(file, on_bad_lines='skip')
        reader.fillna(0, inplace=True)
        for _, row in reader.iterrows():
            new_file = Arrival(
                country_name=row['Country Name'],
                country_code=row['Country Code'],
                a1998=row['1998'],
                a1999=row['1999'],
                a2000=row['2000'],
                a2001=row['2001'],
                a2002=row['2002'],
                a2003=row['2003'],
                a2004=row['2004'],
                a2005=row['2005'],
                a2006=row['2006'],
                a2007=row['2007'],
                a2008=row['2008'],
                a2009=row['2009'],
                a2010=row['2010'],
                a2011=row['2011'],
                a2012=row['2012'],
                a2013=row['2013'],
                a2014=row['2014'],
                a2015=row['2015'],
                a2016=row['2016'],
                a2017=row['2017'],
                a2018=row['2018'],
                a2019=row['2019'],
                a2020=row['2020'],
                a2021=row['2021']
            )
            new_file.save()
        messages.add_message(request, messages.SUCCESS, 'Arrival Data Added Successfully.')
        return redirect('/admins/show_country_by_arrival')
    context = {
        'form': ArrivalForm,
        'activate_country_arrival': 'active bg-primary'
    }
    return render(request, 'admins/add_arrival_csv.html', context)


@login_required(login_url='login')
@admin_only
def delete_arrival(request, country_id):
    country = Arrival.objects.get(id=country_id)
    country.delete()
    messages.add_message(request, messages.SUCCESS, 'Arrival deleted successfully')
    return redirect('/admins/show_country_by_arrival')


@login_required(login_url='login')
@admin_only
def delete_all_arrival(request):
    country = Arrival.objects.all()
    country.delete()
    messages.add_message(request, messages.SUCCESS, 'All arrivals deleted successfully')
    return redirect('/admins/show_country_by_arrival')


@login_required(login_url='login')
@admin_only
def add_expenditure_csv(request):
    if request.method == 'POST':
        file = request.FILES['file']
        reader = pd.read_csv(file, on_bad_lines='skip')
        reader.fillna(0, inplace=True)
        for _, row in reader.iterrows():
            new_file = Expenditure(
                country_name=row['Country Name'],
                country_code=row['Country Code'],
                e1998=row['1998'],
                e1999=row['1999'],
                e2000=row['2000'],
                e2001=row['2001'],
                e2002=row['2002'],
                e2003=row['2003'],
                e2004=row['2004'],
                e2005=row['2005'],
                e2006=row['2006'],
                e2007=row['2007'],
                e2008=row['2008'],
                e2009=row['2009'],
                e2010=row['2010'],
                e2011=row['2011'],
                e2012=row['2012'],
                e2013=row['2013'],
                e2014=row['2014'],
                e2015=row['2015'],
                e2016=row['2016'],
                e2017=row['2017'],
                e2018=row['2018'],
                e2019=row['2019'],
                e2020=row['2020'],
                e2021=row['2021']
            )
            new_file.save()
        messages.add_message(request, messages.SUCCESS, 'Arrival Data Added Successfully.')
        return redirect('/admins/show_country_by_expenditure')
    context = {
        'form': ExpenditureForm,
        'activate_country_expenditure': 'active bg-primary'
    }
    return render(request, 'admins/add_expenditure_csv.html', context)


@login_required(login_url='login')
@admin_only
def delete_expenditure(request, country_id):
    country = Expenditure.objects.get(id=country_id)
    country.delete()
    messages.add_message(request, messages.SUCCESS, 'Expenditure deleted successfully')
    return redirect('/admins/show_country_by_expenditure')


@login_required(login_url='login')
@admin_only
def delete_all_expenditure(request):
    country = Expenditure.objects.all()
    country.delete()
    messages.add_message(request, messages.SUCCESS, 'All expenditures deleted successfully')
    return redirect('/admins/show_country_by_expenditure')


@login_required(login_url='login')
@admin_only
def show_country_by_arrival(request):
    results = Arrival.objects.all()
    result_filter = ArrivalFilter(request.GET, queryset=results)
    result_final = result_filter.qs
    context = {
        'results': result_final,
        'result_filter': result_filter,
        'activate_country_arrival': 'active bg-primary'
    }
    return render(request, 'admins/show_country_by_arrival.html',context)


@login_required(login_url='login')
@admin_only
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
    return render(request, 'admins/show_details_arrival.html',context)


@login_required(login_url='login')
@admin_only
def show_country_by_expenditure(request):
    results = Expenditure.objects.all()
    result_filter = ExpenditureFilter(request.GET, queryset=results)
    result_final = result_filter.qs
    context = {
        'results': result_final,
        'result_filter': result_filter,
        'activate_country_expenditure': 'active bg-primary'
    }
    return render(request, 'admins/show_country_by_expenditure.html',context)


@login_required(login_url='login')
@admin_only
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
    return render(request, 'admins/show_details_expenditure.html',context)


@login_required(login_url='login')
@admin_only
def add_place(request):
    if request.method == 'POST':
        userdata = PlaceForm(request.POST, request.FILES)
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Place Added Successfully.' )
            return redirect('/admins/showplace')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Bad Credentials!' )
            return render(request, 'admins/add_place.html',context)
    context ={'form' : PlaceForm,'activate_place': 'active bg-primary'}
    return render(request, 'admins/add_place.html', context)


@login_required(login_url='login')
@admin_only
def show_place(request):
    results = Places.objects.all()
    result_filter = PlaceFilter(request.GET, queryset=results)
    result_final = result_filter.qs
    context = {
        'results': result_final,
        'result_filter': result_filter,
        'activate_place': 'active bg-primary'
    }
    return render(request, 'admins/show_place.html', context)


@login_required(login_url='login')
@admin_only
def delete_place(request, id):
    country = Places.objects.get(id=id)
    country.delete()
    messages.add_message(request, messages.SUCCESS, 'Place deleted successfully')
    return redirect('/admins/showplace')


@login_required(login_url='login')
@admin_only
def show_details_place(request, id):
    results = Places.objects.get(id=id)
    comments = Comment.objects.filter(place=results.id).order_by('-id')
    context = {
        'results': results,
        'comments': comments,
        'activate_place': 'active bg-primary'
    }
    return render(request, 'admins/show_details_place.html', context)


@login_required(login_url='login')
@admin_only
def update_place(request,id):
    place = Places.objects.get(id=id)
    if request.method == 'POST':
        userdata = PlaceForm(request.POST, request.FILES, instance=place)
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, 'Place Updated Successfully.' )
            return redirect('/admins/show_details_place/'+str(id))
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Bad Credentials!' )
            return render(request, 'admins/update_place.html',context)
    context ={'form' : PlaceForm(instance=place),'activate_place': 'active bg-primary'}
    return render(request, 'admins/update_place.html', context)

@login_required(login_url='login')
@admin_only
def admin_dashboard(request):
    booking = Booking.objects.all()
    booking_count = booking.count()
    country = Country.objects.all()
    country_count = country.count()
    place = Places.objects.all()
    place_count = place.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    user_info = users.filter(is_staff=0)
    admin_info = users.filter(is_staff=1)

    context = {
        'booking': booking_count,
        'country': country_count,
        'place': place_count,
        'user': user_count,
        'admin': admin_count,
        'user_info': user_info,
        'admin_info': admin_info,
        'activate_adminhome': 'active bg-primary'
    }
    return render(request, 'admins/admins_home.html', context)


# Showing all admins
@login_required(login_url='login')
@admin_only
def show_admins(request):
    admins = User.objects.filter(is_staff=1, is_superuser=1).order_by('-id')
    student_filter = UserFilter(request.GET, queryset=admins)
    student_final = student_filter.qs
    context = {
        'results':student_final,
        'student_filter': student_filter,
        'activate_admins': 'active bg-primary'
    }
    return render(request, 'admins/show_admins.html', context)


@login_required(login_url='login')
@admin_only
def show_users(request):
    admins = User.objects.filter(is_staff=0, is_superuser=0).order_by('-id')
    student_filter = UserFilter(request.GET, queryset=admins)
    student_final = student_filter.qs
    context = {
        'results':student_final,
        'student_filter': student_filter,
        'activate_users': 'active bg-primary'
    }
    return render(request, 'admins/show_users.html', context)


@login_required(login_url='login')
@admin_only
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'User deleted successfully')
    return redirect('/admins/showusers')


@login_required(login_url='login')
@admin_only
def delete_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'Admin deleted successfully')
    return redirect('/admins/showadmins')


@login_required(login_url='login')
@admin_only
def booking_data(request):
    booked_data = Booking.objects.all().order_by('-id')
    booking_filter = BookingFilter(request.GET, queryset=booked_data)
    booking_final = booking_filter.qs
    context = {
        'results': booking_final,
        'activate_booking': 'active bg-primary',
        'booking_filter': booking_filter
    }
    return render(request, 'admins/bookingdata.html', context)


@login_required(login_url='login')
@admin_only
def confirm_booking(request, id):
    user = Booking.objects.get(id=id)
    user.status = 'Confirmed'
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Booking confirmed')
    return redirect('/admins/bookingdata')


@login_required(login_url='login')
@admin_only
def deny_booking(request, id):
    user = Booking.objects.get(id=id)
    user.status = 'Denied'
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Booking denied')
    return redirect('/admins/bookingdata')


@login_required(login_url='login')
@admin_only
def contact_form(request):
    contactform = ContactForm.objects.all().order_by('-id')
    context = {
        'contact': contactform
    }
    return render(request, 'admins/contactform.html', context)


@login_required(login_url='login')
@admin_only
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
@admin_only
def add_admin(request):
    if request.method == 'POST':
        form = AddAdmin(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_superuser = True
            user.is_staff = True
            user.save()
            messages.add_message(request, messages.SUCCESS, "New admin has been added in list!")
            return redirect('/admins/showadmins')
        else:
            messages.add_message(request, messages.ERROR, "Error")
            return render(request, 'admins/add_admin.html', {'form':form})
    context = {
        'form': AddAdmin
    }
    return render(request, 'admins/add_admin.html', context)


