from rest_framework import serializers

import logging

from apps.business_app.models.area_node import AreaNode

logger = logging.getLogger(__name__)


class AreaNodeSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(source="area.__str__")
    lon = serializers.DecimalField(
        max_digits=10,
        decimal_places=3,
    )
    lat = serializers.DecimalField(
        max_digits=10,
        decimal_places=3,
    )

    class Meta:
        model = AreaNode
        fields = [
            "id",
            "lat",
            "lon",
            "step",
            "area",
            "area_name",
        ]
