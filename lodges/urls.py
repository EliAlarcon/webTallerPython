from django.urls import path
from . import views

urlpatterns = [
    path('', views.ourEcoLodge, name="ourEcoLodge"),
]