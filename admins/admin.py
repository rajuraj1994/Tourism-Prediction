from django.contrib import admin
from .models import Country,Places
from dashboard.models import Booking

# Register your models here.

admin.site.register(Country)
admin.site.register(Booking)


# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ('Name', 'Description')
#     # list_editable = ('status',)


admin.site.register(Places)
