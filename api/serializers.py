from rest_framework import serializers
from .models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):
    temperature_c = serializers.SerializerMethodField()
    temperature_f = serializers.SerializerMethodField()

    class Meta:
        model = Temperature
        fields = ['id', 'temperature_c', 'temperature_f', 'date']

    def get_temperature_c(self, obj):
        return obj.temperature

    def get_temperature_f(self, obj):
        return (obj.temperature * 1.8) + 32

