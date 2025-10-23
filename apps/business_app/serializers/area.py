from rest_framework import serializers

import logging

from apps.business_app.models.area import Area

logger = logging.getLogger(__name__)


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = [
            "id",
            "name",
            "sub_name",
            "area_type",
            "description",
            "centroid_lat",
            "centroid_lon",
        ]
