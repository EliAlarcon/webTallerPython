from django.shortcuts import render
from . models import Lodge

# Create your views here.
def ourEcoLodge(request):
    lodges =  Lodge.objects.all() 
    return render(request, "lodges/our-eco-lodge.html", {'lodges':lodges})
