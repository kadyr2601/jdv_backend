from django.contrib import admin
from others.models import SEOData, Feedback

admin.site.register(Feedback)

@admin.register(SEOData)
class SEODataAdmin(admin.ModelAdmin):
    readonly_fields = ['og_title', 'og_description', 'og_url']