from django.contrib import admin
from homepage.models import Testimonial, StrategySection, HomePage


admin.site.register(Testimonial)
admin.site.register(StrategySection)

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    readonly_fields = ["og_title", "og_description"]