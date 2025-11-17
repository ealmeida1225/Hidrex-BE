from rest_framework import serializers

import logging

from apps.business_app.models.pluviometer import Pluviometer

logger = logging.getLogger(__name__)


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
            locations = obj.pluviometer_area.select_related("area")
            return [
                {
                    "name": location.area.name,
                    "area_type": location.area.area_type.name
                    if location.area.area_type
                    else None,
                }
                for location in locations
            ]
        except Exception as e:
            logger.error(f"Error retrieving locations for Pluviometer {obj.id}: {e}")
            return []
