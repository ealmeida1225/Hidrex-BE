from rest_framework import serializers

import logging

from apps.business_app.models.area_type import AreaType

logger = logging.getLogger(__name__)


class AreaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaType
        fields = [
            "id",
            "name",
            "representation",
            "description",
        ]
