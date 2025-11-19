from rest_framework import serializers

import logging

from apps.business_app.models.precipitation_concentration_index_monthly_by_area import (
    PrecipitationConcentrationIndexMonthlyByArea,
)

logger = logging.getLogger(__name__)


class PrecipitationConcentrationIndexMonthlyByAreaSerializer(
    serializers.ModelSerializer
):
    area_name = serializers.CharField(source="area.__str__", read_only=True)
    total_rain_value = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    max_rain_value = serializers.DecimalField(max_digits=10, decimal_places=1)
    a_value = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    b_value = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    r_2_value = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )
    ci_value = serializers.DecimalField(
        max_digits=10, decimal_places=2, rounding="ROUND_UP"
    )

    class Meta:
        model = PrecipitationConcentrationIndexMonthlyByArea
        fields = [
            "id",
            "area",
            "area_name",
            "month",
            "years_considered",
            "a_value",
            "b_value",
            "r_2_value",
            "ci_value",
            "rainy_days",
            "total_rain_value",
            "max_rain_value",
            "rainy_days_percent",
            "rain_by_period_avg",
            "rainy_days_by_period_avg",
        ]
