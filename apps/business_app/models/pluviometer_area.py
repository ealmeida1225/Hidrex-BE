from django.db import models

from apps.business_app.models.area import Area
from apps.business_app.models.pluviometer import Pluviometer


class PluviometerArea(models.Model):
    area = models.ForeignKey(Area, models.CASCADE, related_name="pluviometer_area")
    pluviometer = models.ForeignKey(Pluviometer, models.CASCADE, related_name="pluviometer_area")
