from django.shortcuts import render
from django.http import JsonResponse
from .models import SingaporeDistrict


def index(request, id):
    district = SingaporeDistrict.objects.get(id=id)
    return JsonResponse({'name': district.name, 'population': district.population, 'year': district.year})
