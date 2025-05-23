from rest_framework import serializers
from aboutUs.models import AboutUsPage


class AboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPage
        fields = '__all__'
        depth = 1