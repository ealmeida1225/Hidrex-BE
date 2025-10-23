from django.db import models

from apps.business_app.models.area import Area


class AreaNode(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    step = models.IntegerField()
    area = models.ForeignKey(Area, models.CASCADE)
