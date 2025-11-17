from rest_framework import serializers

import logging

from apps.business_app.models.area import Area
from apps.business_app.models.area_node import AreaNode
from apps.business_app.models.pluviometer import Pluviometer

logger = logging.getLogger(__name__)
from django.db.models import Exists, OuterRef


class PluviometerSerializer(serializers.ModelSerializer):
    pluviometer_type_name = serializers.CharField(
        source="pluviometer_type.__str__", read_only=True
    )
    locations = serializers.SerializerMethodField()

    class Meta:
        model = Pluviometer
        fields = [
            "id",
            "name",
            "lat",
            "lon",
            "station_name",
            "msnm",
            "pluviometer_type",
            "pluviometer_type_name",
            "locations",
            "__str__",
        ]

    def get_locations(self, obj):
        try:
            areas = Area.objects.filter(
                Exists(AreaNode.objects.filter(area=OuterRef("pk"))),
                pluviometer_area__pluviometer=obj,
            ).select_related("area_type")
            return [
                {
                    "name": location.name,
                    "area_type": location.area_type.name
                    if location.area_type
                    else None,
                }
                for location in areas
            ]
        except Exception as e:
            logger.error(f"Error retrieving locations for Pluviometer {obj.id}: {e}")
            return []
