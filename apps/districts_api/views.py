from django.shortcuts import render
from django.http import JsonResponse
from .models import SingaporeDistrict


def index(request, id):
    district = SingaporeDistrict.objects.get(id=id)
    return JsonResponse(
        {'name': district.name, 'population': district.population, 'year': district.year, 'gender': district.gender}
    )


def singapore_population(request):
    male_pop = {}
    female_pop = {}
    male_population = SingaporeDistrict.objects.filter(gender__startswith='M')
    female_population = SingaporeDistrict.objects.filter(gender__startswith='F')

    for male in male_population:
        male_pop[male.year] = []
    for male in male_population:
        male_pop[male.year].append({'name': male.name, 'value': male.population})

    for female in female_population:
        female_pop[female.year] = []
    for female in female_population:
        female_pop[female.year].append({'name': female.name, 'value': female.population})
    meta_data = {
        'title': 'Population of Singapore by District',
        'subtext': 'Population of Singapore by District',
        'legend': ["Male", "Female"],
        'x': 'District',
        'y': 'Population',
        'series': [{'name': "Female", 'type': "bar"}, {'name': "Male", 'type': "bar"}]
    }

    return JsonResponse({
        'meta_data': meta_data,
        'dataset_one': male_pop,
        'dataset_two': female_pop
    })
