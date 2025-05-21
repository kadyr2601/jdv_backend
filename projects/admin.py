from django.contrib import admin
from .models import ProjectsPage, Project, ProjectGallery


@admin.register(ProjectsPage)
class ProjectsPageAdmin(admin.ModelAdmin):
    readonly_fields = ["og_title", "og_description"]


class ProjectGalleryAdminInline(admin.StackedInline):
    model = ProjectGallery
    extra = 4


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectGalleryAdminInline,]
    readonly_fields = ["slug"]