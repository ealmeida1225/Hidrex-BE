from rest_framework import serializers

import logging

from apps.business_app.models.month_statistics import MonthStatistics

logger = logging.getLogger(__name__)


class MonthStatisticsSerializer(serializers.ModelSerializer):
    year_name = serializers.CharField(source="year.__str__", read_only=True)
    total_precipit = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    max_registered_value = serializers.DecimalField(max_digits=10, decimal_places=1)
    rainy_streak_med_long = serializers.DecimalField(max_digits=10, decimal_places=2)
    daily_mean = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    rainy_streak_count = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    variance = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    standard_deviation = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )

    class Meta:
        model = MonthStatistics
        fields = [
            "id",
            "max_registered_value",
            "total_precipit",
            "year",
            "year_name",
            "month",
            "variance",
            "standard_deviation",
            "rainy_streak_med_long",
            "rainy_streak_count",
            "rainy_days_count",
            "daily_mean",
        ]
