from rest_framework.response import Response
from rest_framework.views import APIView
from services.models import Service, Maintenance
from services.serializers import ServiceSerializer, MaintenanceSerializer


class ServicesView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class ServiceDetailsView(APIView):
    def get(self, request, slug):
        try:
            # Fetch the Service object
            service = Service.objects.get(slug=slug)
            services_serializer = ServiceSerializer(service)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=404)

        # Fetch related Maintenances
        maintenances = Maintenance.objects.filter(service=service)
        maintenances_serializer = MaintenanceSerializer(maintenances, many=True)

        return Response({
            'service': services_serializer.data,
            'maintenances': maintenances_serializer.data
        })
