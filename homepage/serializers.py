from rest_framework import serializers
from homepage.models import Testimonial, StrategySection, HomePage

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'
        depth = 1