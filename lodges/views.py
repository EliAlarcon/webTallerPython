from django.shortcuts import render, get_object_or_404
from . models import Lodge, Section, DetailSection

# Create your views here.
def ourEcoLodge(request):
    lodges = Lodge.objects.all()
    return render(request, "lodges/our-eco-lodge.html", {'lodges':lodges})

def section(request, section_id):
    sections=get_object_or_404(Section, id=section_id)
    lodges = Lodge.objects.filter(section=sections)
    return render(request, "lodges/our-eco-lodge.html", {'lodges':lodges})
