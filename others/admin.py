from django.contrib import admin
from others.models import ContactPage, Feedback

admin.site.register(Feedback)

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    readonly_fields = ["og_title", "og_description", "banner_image"]