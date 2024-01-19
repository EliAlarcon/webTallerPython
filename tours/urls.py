from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour, name="tour"),
    path('itinerary/<int:itinerary_id>/', views.itinerary, name="itinerary"),
]