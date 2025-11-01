from rest_framework import serializers

import logging

from apps.business_app.models.year_statistics import YearStatistics

logger = logging.getLogger(__name__)


class YearStatisticsSerializer(serializers.ModelSerializer):
    pluviometer_name = serializers.CharField(
        source="pluviometer.__str__", read_only=True
    )

    class Meta:
        model = YearStatistics
        fields = [
            "id",
            "pluviometer",
            "pluviometer_name",
            "year",
            "total_precipit",
            "max_registered_value",
            "daily_mean",
            "rainy_days_count",
            "rainy_streak_count",
            "rainy_streak_med_long",
            "__str__",
        ]
