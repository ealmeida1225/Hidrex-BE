from django.db import models

from apps.business_app.models.area import Area
from apps.business_app.models.pluviometer import Pluviometer


class PluviometerArea(models.Model):
    area = models.ForeignKey(Area, models.CASCADE)
    pluviometer = models.ForeignKey(Pluviometer, models.CASCADE)
