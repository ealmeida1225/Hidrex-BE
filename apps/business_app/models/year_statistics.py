from django.db import models

from apps.business_app.models.pluviometer import Pluviometer


class YearStatistics(models.Model):
    total_precipit = models.FloatField()
    max_registered_value = models.FloatField()
    daily_mean = models.FloatField()
    rainy_days_count = models.PositiveIntegerField()
    rainy_streak_count = models.IntegerField()
    rainy_streak_med_long = models.FloatField()
    pluviometer = models.ForeignKey(Pluviometer, models.DO_NOTHING)
    year = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = "research_yearstatistics"

    def __str__(self):
        return f"{self.pluviometer} ({self.year})"
