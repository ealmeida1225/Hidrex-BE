from rest_framework import serializers

import logging

from apps.business_app.models.year_statistics import YearStatistics

logger = logging.getLogger(__name__)


class YearStatisticsSerializer(serializers.ModelSerializer):
    pluviometer_name = serializers.CharField(
        source="pluviometer.__str__", read_only=True
    )
    total_precipit = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    max_registered_value = serializers.DecimalField(max_digits=10, decimal_places=1)
    rainy_streak_med_long = serializers.DecimalField(max_digits=10, decimal_places=2)
    daily_mean = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
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
