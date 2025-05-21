from rest_framework import serializers
from aboutUs.models import (MainBanner, WelcomeSection, FounderSection, ServicesSection,
                            ServicesBanner, OptionalSection, OptionalBanner, FAQSection)


class MainBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBanner
        fields = '__all__'

class WelcomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeSection
        fields = '__all__'

class FounderSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FounderSection
        fields = '__all__'

class ServicesBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesBanner
        fields = '__all__'
        depth = 1

class ServicesSectionSerializer(serializers.ModelSerializer):
    services_banner = ServicesBannerSerializer(many=True)

    class Meta:
        model = ServicesSection
        fields = '__all__'


class OptionalBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionalBanner
        fields = '__all__'


class OptionalSectionSerializer(serializers.ModelSerializer):
    banners = OptionalBannerSerializer(many=True)

    class Meta:
        model = OptionalSection
        fields = '__all__'

class FAQSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQSection
        fields = '__all__'