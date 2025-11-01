from rest_framework import serializers

import logging

from apps.business_app.models.pluviometer_area import PluviometerArea

logger = logging.getLogger(__name__)


class PluviometerAreaSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(source="area.__str__", read_only=True)
    pluviometer_name = serializers.CharField(
        source="pluviometer.__str__", read_only=True
    )

    class Meta:
        model = PluviometerArea
        fields = [
            "id",
            "area",
            "pluviometer",
            "area_name",
            "pluviometer_name",
        ]
