from django.contrib import admin
from aboutUs.models import (Essence, TeamMember, AboutUsPage)

admin.site.register(Essence)
admin.site.register(TeamMember)

@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    readonly_fields = ["og_title", "og_description"]