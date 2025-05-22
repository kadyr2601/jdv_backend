from rest_framework.views import APIView
from rest_framework.response import Response
from homepage.models import HomePage
from homepage.serializers import HomePageSerializer


class HomePageView(APIView):
    def get(self, request):
        obj = HomePage.objects.first()
        serializer = HomePageSerializer(obj)
        return Response(serializer.data)