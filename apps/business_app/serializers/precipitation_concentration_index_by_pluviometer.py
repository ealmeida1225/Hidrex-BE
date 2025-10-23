from rest_framework import serializers

import logging

from apps.business_app.models.precipitation_concentration_index_by_pluviometer import (
    PrecipitationConcentrationIndexByPluviometer,
)

logger = logging.getLogger(__name__)


class PrecipitationConcentrationIndexByPluviometerSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = PrecipitationConcentrationIndexByPluviometer
        fields = [
            "id",
            "pluviometer",
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
