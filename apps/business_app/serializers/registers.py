from rest_framework import serializers

import logging

from apps.business_app.models.registers import Registers

logger = logging.getLogger(__name__)


class RegistersSerializer(serializers.ModelSerializer):
    pluviometer_name = serializers.CharField(
        source="pluviometer.__str__", read_only=True
    )

    class Meta:
        model = Registers
        fields = [
            "id",
            "pluviometer",
            "pluviometer_name",
            "register_date",
            "rain_value",
        ]
