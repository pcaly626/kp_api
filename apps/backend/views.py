from django.http import JsonResponse
from .test_data.data_female import data_female
from .test_data.data_male import data_male
from . import urls
from .models import SinaporeDistrict

def index(request):
    response = JsonResponse({"test":True})
    response.status_code = 500
    return response

def next_dataset(request):

    # legend and series names need to match
    meta_data = {
        'title':'Next Data',
        'subtext':'Subtext',
        'legend':["Set0", "Set1"],
        'x':'X',
        'y':'Y',
        'series': [{ 'name': "Set0", 'type': "bar" }, { 'name': "Set1", 'type': "bar" }]
        }

    return JsonResponse({'graph_meta_data':meta_data,
                        'dataset_one': {"key": [{'name':'set0','value':1}]}, 
                        'dataset_two': {"key": [{'name':'set1','value':1}]}
                        })

def sinapore_population(request):
    
    # legend and series names need to match
    meta_data = {
        'title':'Population of Singapore by District',
        'subtext':'Population of Singapore by District',
        'legend':["Male", "Female"],
        'x':'District',
        'y':'Population',
        'series': [{ 'name': "Female", 'type': "bar" }, { 'name': "Male", 'type': "bar" }]
        }

    return JsonResponse({'graph_meta_data':meta_data,
                        'dataset_one':data_male, 
                        'dataset_two':data_female
                        })

def list_functions(request):
    endpoints = []
    for url in urls.urlpatterns:
        if str(url.pattern) not in ['', 'list']:
            endpoints.append({'name':str(url.pattern), 'href': f'api/{str(url.pattern)}'})
    return JsonResponse({'endpoints':endpoints})

def one_district(request,id):
    district = SinaporeDistrict.objects.get(id=id)
    print(district)
    return JsonResponse({'name':district.name,'population':district.population})
