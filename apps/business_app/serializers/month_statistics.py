from rest_framework import serializers

import logging

from apps.business_app.models.month_statistics import MonthStatistics

logger = logging.getLogger(__name__)


class MonthStatisticsSerializer(serializers.ModelSerializer):
    year_name = serializers.CharField(source="year.__str__", read_only = True)

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
