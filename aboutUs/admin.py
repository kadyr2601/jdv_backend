from django.contrib import admin
from aboutUs.models import (MainBanner, WelcomeSection, FounderSection, ServicesSection, ServicesBanner,
                            OptionalSection, OptionalBanner, FAQSection)

admin.site.register(MainBanner)
admin.site.register(WelcomeSection)
admin.site.register(FAQSection)
admin.site.register(FounderSection)

class ServicesBannerInline(admin.StackedInline):
    model = ServicesBanner
    extra = 3


@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    inlines = [ServicesBannerInline,]


class OptionalBannerInline(admin.StackedInline):
    model = OptionalBanner
    extra = 3


@admin.register(OptionalSection)
class OptionalSectionAdmin(admin.ModelAdmin):
    inlines = [OptionalBannerInline,]