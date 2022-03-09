from django.http import JsonResponse
from requests.api import get
from .test_data.data_female import data_female
from .test_data.data_male import data_male
from . import urls
from config.keys import keys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import base64

client_credentials_manager =\
    SpotifyClientCredentials(client_id=keys['spotify_id'], client_secret=keys['spotify_secret'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def test_connection(request):
    return JsonResponse({"test_connection":True})

def artists(request):
    meta_data = {
        'title':'Followers to Number of Genres',
        'subtext':'Compare the amount of followers to the artists considered genre',
        'legend':[],
        'x':'NumOfGenres',
        'y':'Followers',
        'series': []
        }

    sp.auth_manager = client_credentials_manager
    response = sp.search(offset=0, type='artist', q="a")
    followers = []
    genres_count = []
    artists = response.get('artists')

    total = artists.get('total', 100)
    items = artists.get('items', [])
    for item in items:
        num_of_genres = len(item['genres'])
        followers.append({'name': num_of_genres, 'value': item['followers']['total']})
        genres_count.append({'name': item['name'], 'value': num_of_genres})

    return JsonResponse({'graph_meta_data':meta_data,
                        'dataset_one': {"Set1": followers},
                        'dataset_two': {}
                        })

def data_schema(request):

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