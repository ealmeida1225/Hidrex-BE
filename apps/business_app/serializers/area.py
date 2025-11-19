from rest_framework import serializers

import logging

from apps.business_app.models.area import Area
from apps.business_app.serializers.area_node import AreaNodeSerializer

logger = logging.getLogger(__name__)


class AreaSerializer(serializers.ModelSerializer):
    area_type_name = serializers.SerializerMethodField()
    nodes = AreaNodeSerializer(many=True, read_only=True)
    centroid_lon = serializers.DecimalField(
        max_digits=10,
        decimal_places=3,
    )
    centroid_lat = serializers.DecimalField(
        max_digits=10,
        decimal_places=3,
    )

    class Meta:
        model = Area
        fields = [
            "id",
            "name",
            "sub_name",
            "area_type",
            "area_type_name",
            "description",
            "centroid_lat",
            "centroid_lon",
            "nodes",
            "__str__",
        ]

    def get_area_type_name(self, object):
        return object.area_type.name if object.area_type else "No definido"
