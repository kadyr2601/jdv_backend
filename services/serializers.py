from rest_framework import serializers
from services.models import Service, Maintenance


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    services = MaintenanceSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = '__all__'