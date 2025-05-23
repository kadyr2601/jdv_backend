from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InteriorDesignService, FitOutService, ArchitectureService
from .serializers import InteriorDesignServiceSerializer, FitOutServiceSerializer, ArchitectureServiceSerializer


class InteriorDesignServiceView(APIView):
    def get(self, request):
        services = InteriorDesignService.objects.first()
        serializer = InteriorDesignServiceSerializer(services)
        return Response(serializer.data)


class FitOutServiceView(APIView):
    def get(self, request):
        services = FitOutService.objects.first()
        serializer = FitOutServiceSerializer(services)
        return Response(serializer.data)


class ArchitectureServiceView(APIView):
    def get(self, request):
        services = ArchitectureService.objects.first()
        serializer = ArchitectureServiceSerializer(services)
        return Response(serializer.data)