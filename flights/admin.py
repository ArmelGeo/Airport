from django.contrib import admin
from .models import Flight

class FlightModelAdmin(admin.ModelAdmin):
    list_filter = ['flight_no', 'status', 'depart_city']
    search_fields = ['fligth_no']
    list_display = ['flight_no', 'depart_city', 'destination_city', 'date', 'status']
    class Meta:
        model = Flight

admin.site.register(Flight, FlightModelAdmin)