from django.db import models

from apps.business_app.models.area_type import AreaType


class Area(models.Model):
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    centroid_lat = models.FloatField()
    area_type = models.ForeignKey(AreaType, models.DO_NOTHING)
    centroid_lon = models.FloatField()

    class Meta:
        managed = False
        db_table = "research_area"

    def __str__(self):
        return self.name
