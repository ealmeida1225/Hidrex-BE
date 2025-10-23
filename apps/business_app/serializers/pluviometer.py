from rest_framework import serializers

import logging

from apps.business_app.models.pluviometer import Pluviometer

logger = logging.getLogger(__name__)


class PluviometerSerializer(serializers.ModelSerializer):
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
        ]
