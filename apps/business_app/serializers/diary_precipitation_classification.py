from rest_framework import serializers

import logging

from apps.business_app.models.diary_precipitation_classification import (
    DiaryPrecipitationClassification,
)

logger = logging.getLogger(__name__)


class DiaryPrecipitationClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryPrecipitationClassification
        fields = [
            "id",
            "lower_limmit",
            "upper_limmit",
            "classification",
        ]
