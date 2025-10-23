from rest_framework import serializers

import logging

from apps.business_app.models.year_statistics import YearStatistics

logger = logging.getLogger(__name__)


class YearStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearStatistics
        fields = [
            "id",
            "pluviometer",
            "year",
            "total_precipit",
            "max_registered_value",
            "daily_mean",
            "rainy_days_count",
            "rainy_streak_count",
            "rainy_streak_med_long",
        ]
