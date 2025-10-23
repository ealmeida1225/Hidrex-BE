from django.db import models

from apps.business_app.models.year_statistics import YearStatistics


class MonthStatistics(models.Model):
    max_registered_value = models.FloatField()
    daily_mean = models.FloatField()
    rainy_days_count = models.PositiveIntegerField()
    rainy_streak_count = models.IntegerField()
    rainy_streak_med_long = models.FloatField()
    standard_deviation = models.FloatField()
    variance = models.FloatField()
    month = models.PositiveSmallIntegerField()
    year = models.ForeignKey(YearStatistics, models.CASCADE)
    total_precipit = models.FloatField()
