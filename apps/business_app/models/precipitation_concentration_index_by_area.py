from django.db import models

from apps.business_app.models.area import Area


class PrecipitationConcentrationIndexByArea(models.Model):
    years_considered = models.PositiveSmallIntegerField()
    a_value = models.FloatField()
    b_value = models.FloatField()
    r_2_value = models.FloatField()
    ci_value = models.FloatField()
    rainy_days = models.PositiveIntegerField()
    max_rain_value = models.FloatField()
    rainy_days_percent = models.FloatField()
    rain_by_period_avg = models.FloatField()
    rainy_days_by_period_avg = models.TextField()
    area = models.ForeignKey(Area, models.DO_NOTHING)
    total_rain_value = models.FloatField()

    class Meta:
        managed = False
        db_table = "research_precipitationconcentrationindexbyarea"
