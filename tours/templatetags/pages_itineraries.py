from tours.models import Itinerary
from django import template

register=template.Library()

@register.simple_tag
def get_pages():
    pages=Itinerary.objects.all()
    return pages