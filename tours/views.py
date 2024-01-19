from django.shortcuts import render, get_object_or_404
from . models import Tour, Itinerary

# Create your views here.
def tour(request):
    tours =  Tour.objects.all() 
    return render(request, "tours/tour.html", {'tours':tours})

def itinerary(request, itinerary_id):
    page=get_object_or_404(Itinerary, id=itinerary_id)
    return render(request, "tours/itinerary.html",{'page': page})