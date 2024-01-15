from django.shortcuts import render
from . models import Tour

# Create your views here.
def tour(request):
    tours =  Tour.objects.all() 
    return render(request, "tours/tour.html", {'tours':tours})