from rest_framework import serializers

import logging

from apps.business_app.models.precipitation_concentration_index_monthly_by_area import (
    PrecipitationConcentrationIndexMonthlyByArea,
)

logger = logging.getLogger(__name__)


class PrecipitationConcentrationIndexMonthlyByAreaSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = PrecipitationConcentrationIndexMonthlyByArea
        fields = [
            "id",
            "area",
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
