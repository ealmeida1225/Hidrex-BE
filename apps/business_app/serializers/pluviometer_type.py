from rest_framework import serializers

import logging

from apps.business_app.models.pluviometer import Pluviometer
from apps.business_app.models.pluviometer_type import PluviometerType

logger = logging.getLogger(__name__)


class PluviometerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PluviometerType
        fields = [
            "id",
            "name",
            "description",
        ]
