from rest_framework import serializers

import logging

from apps.business_app.models.area_node import AreaNode

logger = logging.getLogger(__name__)


class AreaNodeSerializer(serializers.ModelSerializer):
    area_name = serializers.CharField(source="area.__str__")

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
