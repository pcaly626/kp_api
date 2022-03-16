from django.db import models


class SinaporeDistrict(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    population = models.IntegerField()