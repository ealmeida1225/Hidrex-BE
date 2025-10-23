from django.db import models

from apps.business_app.models.pluviometer import Pluviometer


class Registers(models.Model):
    register_date = models.DateField()
    rain_value = models.FloatField()
    pluviometer = models.ForeignKey(Pluviometer, models.CASCADE)
