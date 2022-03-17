import os, django
from test_data.data_male import data_male
from test_data.data_female import data_female
from apps.districts_api.models import SinaporeDistrict

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()



def add_data(data_set):
    for year in data_set:
        for data in data_set[year]:
            district = SinaporeDistrict.objects.create( year=year, name=data['name'], population=data['value'] )
            district.save()

if name == 'main':
    add_data(data_male)
    add_data(data_female)

