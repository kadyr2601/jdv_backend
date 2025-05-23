from rest_framework import views, generics
from rest_framework.response import Response
from others.serializers import FeedbackSerializer, ContactPageSerializer
from others.models import ContactPage


class FeedbackView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer


class ContactPageView(views.APIView):
    def get(self, request):
        data = ContactPage.objects.first()
        serializer = ContactPageSerializer(data)
        return Response(serializer.data)