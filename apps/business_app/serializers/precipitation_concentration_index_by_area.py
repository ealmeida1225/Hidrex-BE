from rest_framework import serializers

import logging

from apps.business_app.models.precipitation_concentration_index_by_area import (
    PrecipitationConcentrationIndexByArea,
)

logger = logging.getLogger(__name__)


class PrecipitationConcentrationIndexByAreaSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(source="area.__str__", read_only=True)

    class Meta:
        model = PrecipitationConcentrationIndexByArea
        fields = [
            "id",
            "area",
            "area_name",
            "years_considered",
            "a_value",
            "b_value",
            "r_2_value",
            "ci_value",
            "rainy_days",
            "max_rain_value",
            "rainy_days_percent",
            "rain_by_period_avg",
            "rainy_days_by_period_avg",
            "total_rain_value",
        ]
