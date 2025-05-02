from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from homepage.serializers import AboutSectionSerializer, FeaturedServicesSectionSerializer, ReviewsSectionSerializer, \
    BeforeAfterSectionSerializer, FeaturedProjectsSectionSerializer, LuxuryBannerSerializer, \
    AboutInteriorSectionSerializer
from homepage.models import (
    AboutSection,
    FeaturedServicesSection,
    ReviewsSection,
    BeforeAfterSection,
    FeaturedProjectsSection,
    AboutInteriorSection, LuxuryBanner,
)


class HomePageView(APIView):
    def get(self, request):
        try:
            banner = LuxuryBanner.objects.first()
            banner_ser = LuxuryBannerSerializer(banner) if banner else None

            about = AboutSection.objects.first()
            about_ser = AboutSectionSerializer(about) if about else None

            featured_services = FeaturedServicesSection.objects.first()
            featured_services_ser = FeaturedServicesSectionSerializer(featured_services) if featured_services else None

            reviews = ReviewsSection.objects.all()
            reviews_ser = ReviewsSectionSerializer(reviews, many=True) if reviews else None

            before_after = BeforeAfterSection.objects.first()
            before_after_ser = BeforeAfterSectionSerializer(before_after) if before_after else None

            featured_projects = FeaturedProjectsSection.objects.all()
            featured_projects_ser = FeaturedProjectsSectionSerializer(featured_projects, many=True) if featured_projects else None

            about_interior = AboutInteriorSection.objects.first()
            about_interior_ser = AboutInteriorSectionSerializer(about_interior) if about_interior else None

        except ObjectDoesNotExist:
            about_ser = None
            featured_services_ser = None
            reviews_ser = None
            before_after_ser = None
            featured_projects_ser = None
            about_interior_ser = None

        data = {
            'banner': banner_ser.data if banner_ser else None,
            "about_section": about_ser.data if about_ser else None,
            "featured_services": featured_services_ser.data if featured_services_ser else None,
            "reviews": reviews_ser.data if reviews_ser else None,
            "before_after": before_after_ser.data if before_after_ser else None,
            "featured_projects": featured_projects_ser.data if featured_projects_ser else None,
            "about_interior": about_interior_ser.data if about_interior_ser else None,
        }
        return Response(data)
