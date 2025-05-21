from django.contrib import admin
from homepage.models import (BannerCTA, BannerSlide, LuxuryBanner, AboutSection, AboutSectionBanner, FeaturedServicesSection,
                             FeaturedServicesBanner, ReviewsSection, BeforeAfterSection, FeaturedProjectsSection,
                             AboutInteriorSection, AboutInteriorBanner)


admin.site.register(BannerCTA)
admin.site.register(BannerSlide)
admin.site.register(LuxuryBanner)


class AboutSectionInline(admin.StackedInline):
    model = AboutSectionBanner
    extra = 3


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    inlines = [AboutSectionInline,]


class FeaturedServicesBannerInline(admin.StackedInline):
    model = FeaturedServicesBanner
    extra = 3


@admin.register(FeaturedServicesSection)
class FeaturedServicesSectionAdmin(admin.ModelAdmin):
    inlines = [FeaturedServicesBannerInline,]


admin.site.register(ReviewsSection)
admin.site.register(BeforeAfterSection)
admin.site.register(FeaturedProjectsSection)


class AboutInteriorBannerInline(admin.StackedInline):
    model = AboutInteriorBanner
    extra = 2


@admin.register(AboutInteriorSection)
class AboutInteriorSectionAdmin(admin.ModelAdmin):
    inlines = [AboutInteriorBannerInline,]