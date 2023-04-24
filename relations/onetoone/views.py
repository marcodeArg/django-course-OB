from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def create(request):
    place = Place(name = 'Place 1', address = 'Demo Address')
    place.save()

    restaurant = Restaurant(place = place, number_employees = 14)
    restaurant.save()

    message = restaurant.place.name + ' have ' + str(restaurant.number_employees) + ' employees'

    return HttpResponse(message)