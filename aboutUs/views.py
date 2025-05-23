from rest_framework.response import Response
from rest_framework.views import APIView
from aboutUs.models import AboutUsPage
from aboutUs.serializers import AboutUsPageSerializer

class AboutUsPageView(APIView):
    def get(self, request):
        page = AboutUsPage.objects.first()
        serializer = AboutUsPageSerializer(page)
        return Response(serializer.data)