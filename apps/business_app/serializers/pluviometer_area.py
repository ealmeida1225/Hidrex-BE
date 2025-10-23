from rest_framework import serializers

import logging

from apps.business_app.models.pluviometer_area import PluviometerArea

logger = logging.getLogger(__name__)


class PluviometerAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PluviometerArea
        fields = [
            "id",
            "area",
            "pluviometer",
        ]
