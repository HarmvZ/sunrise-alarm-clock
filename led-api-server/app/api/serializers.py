from alarms.models import AlarmConfig
from rest_framework import serializers


class AlarmConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmConfig
        fields = [
            "pk",
            "colors",
            "playlist",
            "volumes",
            "duration",
        ]
