from django.db import models

from apps.business_app.models.pluviometer_type import PluviometerType


class Pluviometer(models.Model):
    name = models.CharField(max_length=15)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    station_name = models.CharField(max_length=100, blank=True, null=True)
    msnm = models.IntegerField(blank=True, null=True)
    pluviometer_type = models.ForeignKey(
        PluviometerType, models.DO_NOTHING, blank=True, null=True
    )

    def __str__(self):
        return f"{self.station_name} ({self.name})"
