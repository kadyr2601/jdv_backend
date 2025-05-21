from rest_framework import serializers
from homepage.models import (
    AboutSection,
    AboutSectionBanner,
    FeaturedServicesSection,
    FeaturedServicesBanner,
    ReviewsSection,
    BeforeAfterSection,
    FeaturedProjectsSection,
    AboutInteriorSection,
    AboutInteriorBanner,
    BannerCTA, BannerSlide, LuxuryBanner
)


class BannerCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerCTA
        fields = "__all__"


class BannerSlideSerializer(serializers.ModelSerializer):
    cta = BannerCTASerializer(allow_null=True)

    class Meta:
        model = BannerSlide
        fields = "__all__"


class LuxuryBannerSerializer(serializers.ModelSerializer):
    slides = BannerSlideSerializer(many=True)

    class Meta:
        model = LuxuryBanner
        fields = "__all__"


class AboutSectionBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSectionBanner
        fields = '__all__'

class AboutSectionSerializer(serializers.ModelSerializer):
    about_banner_set = AboutSectionBannerSerializer(many=True, read_only=True)

    class Meta:
        model = AboutSection
        fields = '__all__'

class FeaturedServicesBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedServicesBanner
        fields = '__all__'
        depth = 1

class FeaturedServicesSectionSerializer(serializers.ModelSerializer):
    services_banner_set = FeaturedServicesBannerSerializer(many=True, read_only=True)

    class Meta:
        model = FeaturedServicesSection
        fields = '__all__'

class ReviewsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsSection
        fields = '__all__'

class BeforeAfterSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeforeAfterSection
        fields = '__all__'

class FeaturedProjectsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedProjectsSection
        fields = '__all__'
        depth = 1

class AboutInteriorBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInteriorBanner
        fields = '__all__'

class AboutInteriorSectionSerializer(serializers.ModelSerializer):
    about_interior_banner_set = AboutInteriorBannerSerializer(many=True, read_only=True)

    class Meta:
        model = AboutInteriorSection
        fields = '__all__'