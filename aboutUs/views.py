from rest_framework.response import Response
from rest_framework.views import APIView
from aboutUs.models import MainBanner, WelcomeSection, FounderSection, ServicesSection, OptionalSection, FAQSection
from aboutUs.serializers import (MainBannerSerializer, WelcomeSectionSerializer, FounderSectionSerializer,
                                 OptionalSectionSerializer, FAQSectionSerializer, ServicesSectionSerializer)

class AboutUsPageView(APIView):
    def get(self, request):
        banner = MainBanner.objects.first()
        welcome_section = WelcomeSection.objects.first()
        founder_section = FounderSection.objects.first()
        services_section = ServicesSection.objects.first()
        optional_section = OptionalSection.objects.first()
        faq_section = FAQSection.objects.all()

        return Response({
            'banner': MainBannerSerializer(banner).data if banner else None,
            'welcome_section': WelcomeSectionSerializer(welcome_section).data if welcome_section else None,
            'founder_section': FounderSectionSerializer(founder_section).data if founder_section else None,
            'services_section': ServicesSectionSerializer(services_section).data if services_section else None,
            'optional_section': OptionalSectionSerializer(optional_section).data if optional_section else None,
            'faq_section': FAQSectionSerializer(faq_section, many=True).data if faq_section.exists() else None
        })