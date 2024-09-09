from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    country_name = models.CharField(max_length=120, null=True, unique=True)
    country_code = models.CharField(max_length=10, null=True, unique=True)

    def __str__(self):
        return self.country_name


class CountryCSV(models.Model):
    file = models.FileField(upload_to="static/uploads/data", null=True)


class Arrival(models.Model):
    country_name = models.CharField(max_length=120, null=True, unique=True)
    country_code = models.CharField(max_length=10, null=True, unique=True)
    indicator_name = models.CharField(max_length=200, null=True)
    a1998 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a1999 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2000 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2001 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2002 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2003 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2004 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2005 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2006 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2007 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2008 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2009 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2010 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2011 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2012 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2013 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2014 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2015 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2016 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2017 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2018 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2019 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2020 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    a2021 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)


class ArrivalCSV(models.Model):
    file = models.FileField(upload_to="static/uploads/data", null=True)


class Expenditure(models.Model):
    country_name = models.CharField(max_length=120, null=True, unique=True)
    country_code = models.CharField(max_length=10, null=True, unique=True)
    indicator_name = models.CharField(max_length=200, null=True)
    e1998 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e1999 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2000 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2001 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2002 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2003 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2004 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2005 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2006 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2007 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2008 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2009 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2010 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2011 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2012 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2013 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2014 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2015 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2016 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2017 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2018 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2019 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2020 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)
    e2021 = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True)


class ExpenditureCSV(models.Model):
    file = models.FileField(upload_to="static/uploads/data", null=True)


class Places(models.Model):
    place_name = models.CharField(max_length=200, null=True)
    place_location = models.CharField(max_length=200, null=True)
    place_desc = models.TextField(null=True)
    country = models.ForeignKey(Country, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    total_days = models.IntegerField(null=True)
    place_image = models.FileField(upload_to="static/uploads/data", null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    total_rating = models.DecimalField(decimal_places=2, max_digits=30, null=True, blank=True, default=0.00)
    total_comments = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.place_name


class Comment(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    place = models.ForeignKey(Places, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    rating = models.CharField(max_length=10, choices=RATING)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
