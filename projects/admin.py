from django.contrib import admin
from .models import Project, ProjectGallery, MainBanner

admin.site.register(MainBanner)


class ProjectGalleryAdminInline(admin.StackedInline):
    model = ProjectGallery
    extra = 4


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectGalleryAdminInline,]
    readonly_fields = ["slug"]