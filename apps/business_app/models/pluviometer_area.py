from django.db import models

from apps.business_app.models.area import Area
from apps.business_app.models.pluviometer import Pluviometer


class PluviometerArea(models.Model):
    area = models.ForeignKey(Area, models.DO_NOTHING)
    pluviometer = models.ForeignKey(Pluviometer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "research_pluviometerarea"
