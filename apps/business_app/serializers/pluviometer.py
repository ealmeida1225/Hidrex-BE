from rest_framework import serializers

import logging

from apps.business_app.models.pluviometer import Pluviometer

logger = logging.getLogger(__name__)


class PluviometerSerializer(serializers.ModelSerializer):
    pluviometer_type_name = serializers.CharField(source="pluviometer_type.__str__")
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
            "__str__",
        ]
