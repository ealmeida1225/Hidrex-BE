from rest_framework import serializers

import logging

from apps.business_app.models.registers import Registers

logger = logging.getLogger(__name__)


class RegistersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registers
        fields = [
            "id",
            "pluviometer",
            "register_date",
            "rain_value",
        ]
