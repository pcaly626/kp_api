import os, django
from test_data.data_male import data_male
from test_data.data_female import data_female

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.districts_api.models import SingaporeDistrict


def add_data(data_set, gender):
    for year in data_set:
        for data in data_set[year]:
            district = SingaporeDistrict.objects.create(
                year=year,
                name=data['name'],
                population=data['value'],
                gender=gender
            )
            district.save()


if __name__ == '__main__':
    add_data(data_male, 'M')
    add_data(data_female, 'F')
