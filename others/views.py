from rest_framework import views, generics, status
from rest_framework.response import Response
from others.serializers import FeedbackSerializer, SEODataSerializer
from others.models import SEOData


class FeedbackView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer


class SEOView(views.APIView):
    def get(self, request, page):
        try:
            seo_data = SEOData.objects.get(page=page)
            serializer = SEODataSerializer(seo_data)
            return Response(serializer.data)
        except SEOData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)