from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Flight
from .forms import FlightForm
from django.db.models import Q

#from django.views.generic import ListView  
#from django.views.generic.edit import CreateView, UpdateView, DeleteView  
#from django.core.urlresolvers import reverse_lazy


def flights_list(request): #homepage
    flights = Flight.objects.all()
    query = request.GET.get("flights")
    or_lookup = (Q(status__icontains=query) | Q(depart_city__icontains=query) | Q(destination_city__icontains=query))
    if query:
        flights = Flight.objects.filter(or_lookup)

    return render(request, "flights/flight_list.html", {'object_list': flights})

def flights_details(request, id=None):
    instance = get_object_or_404(Flight, id=id)

    return render(request, 'flights/flight_detail.html', {'obj': instance })

def flight_new(request):
    form = FlightForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        redirect('flights:flight_list')  

    return render(request, "flights/flight_form.html", {'form': form})


def flight_update(request, id=None):
    instance = get_object_or_404(Flight, id=id)
    form = FlightForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('flights:flight_list')  
    context = {
        'instance': instance,
        'form': form,
    }
    return render(request, "flights/flight_form.html", context)


def flight_delete(request, id=None):
    instance = get_object_or_404(Flight, id=id)
    form = FlightForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance.delete()
        return redirect('flights:flight_list')  
    context = {
        'instance': instance,
        'form': form,
    }
    return render(request, "flights/flight_form.html", context)


"""
class FlightList(ListView):  
     model = Flight  
   
   
class FlightCreate(CreateView):  
    model = Flight  
    fields = ['fligth_no', 'depart_city', 'destination_city', 'date', 'date_time', 'status']
    success_url = reverse_lazy('flights: flight_list')  
   
   
class FlightUpdate(UpdateView):  
    model = Flight   
    fields = ['fligth_no', 'depart_city', 'destination_city', 'date', 'date_time', 'status']
    success_url = reverse_lazy('flights: flight_list')  
   
   
class FlightDelete(DeleteView):  
    model = Flight    
    success_url = reverse_lazy('flights: flight_list') 
"""

