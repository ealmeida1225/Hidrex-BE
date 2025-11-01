from rest_framework import serializers

import logging

from apps.business_app.models.area import Area

logger = logging.getLogger(__name__)


class AreaSerializer(serializers.ModelSerializer):
    area_type_name = serializers.SerializerMethodField()

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
            "__str__",
        ]

    def get_area_type_name(self, object):
        return object.area_type.name if object.area_type else "No definido"
