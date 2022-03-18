from django.db import models


class SingaporeDistrict(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', 'MALE',
        FEMALE = 'F', 'FEMALE'

    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    population = models.IntegerField()
    gender = models.CharField(max_length=4, choices=Gender.choices)


