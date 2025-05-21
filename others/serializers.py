from rest_framework import serializers
from others.models import SEOData, Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class SEODataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEOData
        fields = '__all__'